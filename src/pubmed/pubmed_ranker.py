from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import Iterable

from src.llm.provider_base import Claim, RerankResult
from src.pubmed.eutils_client import PubMedPaper


def heuristic_score(paper: PubMedPaper, query_terms: Iterable[str]) -> float:
    score = 0.0
    year = int(paper.year) if paper.year.isdigit() else 0
    if year:
        age = max(0, datetime.now().year - year)
        score += max(0.0, 1.0 - (age / 25.0))
    pub_types = " ".join(paper.pub_types).lower()
    if "meta-analysis" in pub_types:
        score += 1.2
    if "review" in pub_types or "systematic" in pub_types:
        score += 0.8
    text = f"{paper.title} {paper.abstract}".lower()
    for t in query_terms:
        if t and t.lower() in text:
            score += 0.1
    if paper.abstract:
        score += 0.1
    return score


def combine_scores(
    papers: list[PubMedPaper],
    llm_results: list[RerankResult],
    claims: list[Claim],
    k: int,
) -> list[tuple[PubMedPaper, list[int], str, float]]:
    by_pmid = {p.pmid: p for p in papers}
    llm_by_pmid = {r.pmid: r for r in llm_results if r.pmid}

    ranked: list[tuple[PubMedPaper, list[int], str, float]] = []
    for pmid, paper in by_pmid.items():
        lr = llm_by_pmid.get(pmid)
        llm_score = lr.score if lr else 0.0
        heur = heuristic_score(paper, [])
        total = heur + (2.0 * llm_score)
        supported = lr.supported_claim_indices if lr else []
        rationale = lr.rationale if lr else "heuristic only"
        ranked.append((paper, supported, rationale, total))

    ranked.sort(key=lambda x: x[3], reverse=True)

    selected: list[tuple[PubMedPaper, list[int], str, float]] = []
    claim_coverage = defaultdict(int)
    for item in ranked:
        if len(selected) >= k:
            break
        _, supported, _, _ = item
        diversity_bonus = sum(1 for idx in supported if claim_coverage[idx] == 0)
        if selected and diversity_bonus == 0 and len(selected) < k - 1:
            continue
        selected.append(item)
        for idx in supported:
            claim_coverage[idx] += 1

    if len(selected) < k:
        for item in ranked:
            if item in selected:
                continue
            selected.append(item)
            if len(selected) >= k:
                break
    return selected[:k]
