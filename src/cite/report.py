from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.cite.apa_formatter import format_apa_journal_article
from src.cite.inserter import FootnoteAssignment
from src.pubmed.eutils_client import PubMedPaper


def write_outputs(
    outdir: Path,
    english_sentences: list[str],
    original_sentences: list[str],
    assignments: list[FootnoteAssignment],
    papers_by_pmid: dict[str, PubMedPaper],
    supported_claims: dict[str, list[str]],
    queries_used: dict[str, list[str]],
) -> dict[str, Path]:
    outdir.mkdir(parents=True, exist_ok=True)

    def bibliography_lines() -> list[str]:
        lines = ["", "## References"]
        for a in assignments:
            paper = papers_by_pmid[a.pmid]
            lines.append(f"[^${a.footnote_number}]: {format_apa_journal_article(paper)}".replace("$", ""))
        return lines

    eng_md = "\n\n".join(english_sentences) + "\n" + "\n".join(bibliography_lines()) + "\n"
    ori_md = "\n\n".join(original_sentences) + "\n" + "\n".join(bibliography_lines()) + "\n"

    english_path = outdir / "english_annotated.md"
    original_path = outdir / "original_annotated.md"
    english_path.write_text(eng_md, encoding="utf-8")
    original_path.write_text(ori_md, encoding="utf-8")

    report_lines = ["# Citation Report", ""]
    jsonl_path = outdir / "citations.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as jf:
        for a in assignments:
            p = papers_by_pmid[a.pmid]
            snippets = [english_sentences[i][:160] for i in a.sentence_indices if i < len(english_sentences)]
            report_lines.append(f"## [^{a.footnote_number}] PMID {p.pmid}")
            report_lines.append(f"- Title: {p.title}")
            report_lines.append(f"- Inserted sentence indices: {a.sentence_indices}")
            report_lines.append(f"- Snippets: {snippets}")
            report_lines.append(f"- Supported claims: {supported_claims.get(p.pmid, [])}")
            report_lines.append("")
            record: dict[str, Any] = {
                "footnote_number": a.footnote_number,
                "pmid": p.pmid,
                "doi": p.doi,
                "title": p.title,
                "authors": p.authors,
                "year": p.year,
                "journal": p.journal,
                "url": f"https://doi.org/{p.doi}" if p.doi else f"https://pubmed.ncbi.nlm.nih.gov/{p.pmid}/",
                "abstract_snippet": p.abstract[:280],
                "queries_used": queries_used.get(p.pmid, []),
                "supported_sentence_indices": a.sentence_indices,
                "supported_claims": supported_claims.get(p.pmid, []),
            }
            jf.write(json.dumps(record, ensure_ascii=False) + "\n")

    report_path = outdir / "citation_report.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    return {
        "english": english_path,
        "original": original_path,
        "report": report_path,
        "jsonl": jsonl_path,
    }
