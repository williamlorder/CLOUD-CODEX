from __future__ import annotations

from src.pubmed.eutils_client import PubMedPaper


def _format_authors(authors: list[str], max_authors: int = 20) -> str:
    if not authors:
        return ""
    trimmed = authors[:max_authors]
    formatted = []
    for a in trimmed:
        if " " in a:
            last, initials = a.split(" ", 1)
            initials_fmt = ". ".join(list(initials)) + "." if initials else ""
            formatted.append(f"{last}, {initials_fmt}".strip())
        else:
            formatted.append(a)
    if len(formatted) == 1:
        return formatted[0]
    return ", ".join(formatted[:-1]) + ", & " + formatted[-1]


def format_apa_journal_article(paper: PubMedPaper) -> str:
    authors = _format_authors(paper.authors)
    year = paper.year or "n.d."
    title = paper.title.rstrip(".") + "." if paper.title else ""
    journal = paper.journal
    vol_issue = paper.volume
    if paper.issue:
        vol_issue += f"({paper.issue})"
    pages = f", {paper.pages}" if paper.pages else ""
    url = f"https://doi.org/{paper.doi}" if paper.doi else f"https://pubmed.ncbi.nlm.nih.gov/{paper.pmid}/"
    main = f"{authors} ({year}). {title} {journal}"
    if vol_issue:
        main += f", {vol_issue}"
    main += pages + "."
    return f"{main} {url}".strip()
