from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from src.cite.inserter import FootnoteAssignment, insert_footnotes
from src.cite.report import write_outputs
from src.llm.gemini_provider import GeminiProvider
from src.llm.openai_provider import OpenAIProvider
from src.llm.provider_base import Claim, LLMProvider
from src.pubmed.eutils_client import EUtilsClient, PubMedPaper
from src.pubmed.pubmed_ranker import combine_scores
from src.utils.lang_detect import is_chinese_text
from src.utils.sentence_split import split_sentences


def baseline_query_from_text(text: str, n: int = 10) -> str:
    tokens = [t.lower().strip(".,;:()[]{}\"'") for t in text.split()]
    tokens = [t for t in tokens if len(t) > 4]
    uniq = []
    for t in tokens:
        if t not in uniq:
            uniq.append(t)
    return " AND ".join(uniq[:n])


def load_config(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    txt = p.read_text(encoding="utf-8")
    if p.suffix.lower() in {".json"}:
        return json.loads(txt)
    if p.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore

            return yaml.safe_load(txt) or {}
        except ImportError:
            raise RuntimeError("YAML config requested but PyYAML is not installed")
    return {}


def build_provider(provider: str, config: dict[str, Any]) -> LLMProvider:
    llm_cfg = config.get("llm", {})
    if provider == "openai":
        return OpenAIProvider(model=llm_cfg.get("openai_model", "gpt-4o-mini"), base_url=llm_cfg.get("openai_base_url", "https://api.openai.com/v1"))
    if provider == "gemini":
        return GeminiProvider(model=llm_cfg.get("gemini_model", "gemini-1.5-flash"))
    raise ValueError(f"Unsupported provider: {provider}")


def widen_queries(queries: list[str]) -> list[str]:
    widened = []
    for q in queries:
        widened.append(q)
        widened.append(q.replace("[Title/Abstract]", "").replace("AND", "OR"))
    return list(dict.fromkeys(widened))


def map_papers_to_sentences(claims: list[Claim], claim_indices: list[int]) -> list[int]:
    sentence_ids: set[int] = set()
    for ci in claim_indices:
        if 0 <= ci < len(claims):
            sentence_ids.update(claims[ci].sentence_indices)
    return sorted(sentence_ids)


def run_pipeline(args: argparse.Namespace) -> dict[str, Path]:
    load_dotenv()
    config = load_config(args.config)

    if args.input_file:
        text = Path(args.input_file).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    if not text.strip():
        raise ValueError("Input text is empty")

    provider = build_provider(args.provider, config)

    zh = is_chinese_text(text)
    original_sentences = split_sentences(text, chinese=zh)
    if zh:
        english_sentences = provider.translate(original_sentences)
        if len(english_sentences) != len(original_sentences):
            english_sentences = english_sentences[: len(original_sentences)] + original_sentences[len(english_sentences) :]
    else:
        english_sentences = original_sentences[:]

    english_text = " ".join(english_sentences)

    claims = provider.extract_claims(english_text, len(english_sentences))
    query_bundle = provider.generate_queries(english_text)
    baseline_q = baseline_query_from_text(english_text)
    queries = list(dict.fromkeys(query_bundle.queries + [query_bundle.baseline_query, baseline_q]))

    pub_cfg = config.get("pubmed", {})
    retmax = int(pub_cfg.get("retmax", 80))
    client = EUtilsClient(email=args.email, tool=pub_cfg.get("tool", "cloud-codex-citer"))

    pmids: list[str] = []
    queries_used: dict[str, list[str]] = defaultdict(list)
    for q in queries:
        ids = client.esearch(q, retmax=retmax)
        for pid in ids:
            queries_used[pid].append(q)
        pmids.extend(ids)

    unique_pmids = list(dict.fromkeys(pmids))
    if len(unique_pmids) < max(5, args.k):
        for q in widen_queries(queries):
            ids = client.esearch(q, retmax=retmax)
            for pid in ids:
                queries_used[pid].append(q)
            unique_pmids.extend(ids)
        unique_pmids = list(dict.fromkeys(unique_pmids))

    candidate_pmids = unique_pmids[: int(pub_cfg.get("max_candidates", 200))]
    papers = client.efetch(candidate_pmids)
    paper_dict = {p.pmid: p for p in papers if p.pmid}

    llm_candidates = [
        {"pmid": p.pmid, "title": p.title, "journal": p.journal, "year": p.year, "abstract": p.abstract[:800], "pub_types": p.pub_types}
        for p in papers
    ]
    reranked = provider.rerank(english_text, claims, llm_candidates)
    selected = combine_scores(papers, reranked, claims, args.k)

    assignments: list[FootnoteAssignment] = []
    supported_claims: dict[str, list[str]] = {}
    for i, (paper, claim_idxs, _rationale, _score) in enumerate(selected, start=1):
        sentence_indices = map_papers_to_sentences(claims, claim_idxs)
        if not sentence_indices:
            sentence_indices = [0] if english_sentences else []
        assignments.append(FootnoteAssignment(footnote_number=i, pmid=paper.pmid, sentence_indices=sentence_indices))
        supported_claims[paper.pmid] = [claims[c].claim for c in claim_idxs if 0 <= c < len(claims)]

    english_annotated = insert_footnotes(english_sentences, assignments)
    original_annotated = insert_footnotes(original_sentences, assignments)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = Path(args.outdir) / timestamp
    paths = write_outputs(
        outdir=outdir,
        english_sentences=english_annotated,
        original_sentences=original_annotated,
        assignments=assignments,
        papers_by_pmid=paper_dict,
        supported_claims=supported_claims,
        queries_used=queries_used,
    )
    print(f"Inserted {len(assignments)} citations. Output dir: {outdir}")
    for k, p in paths.items():
        print(f"- {k}: {p}")
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Annotate academic text with PubMed-backed citations")
    parser.add_argument("--provider", choices=["openai", "gemini"], required=True)
    parser.add_argument("--k", type=int, default=8)
    parser.add_argument("--input-file", type=str)
    parser.add_argument("--outdir", type=str, default="outputs")
    parser.add_argument("--email", type=str, required=True)
    parser.add_argument("--config", type=str, default=None)
    args = parser.parse_args()
    if not (1 <= args.k <= 50):
        parser.error("--k must be between 1 and 50")
    return args


if __name__ == "__main__":
    run_pipeline(parse_args())
