from src.cite.apa_formatter import format_apa_journal_article
from src.pubmed.eutils_client import PubMedPaper


def test_apa_with_doi():
    paper = PubMedPaper(
        pmid="123",
        title="Sleep and memory",
        authors=["Smith AB", "Jones CD"],
        journal="Journal of Sleep",
        year="2020",
        volume="10",
        issue="2",
        pages="100-110",
        doi="10.1000/j.jos.2020.01",
        abstract="",
        pub_types=[],
    )
    out = format_apa_journal_article(paper)
    assert "https://doi.org/10.1000/j.jos.2020.01" in out
    assert "(2020)." in out


def test_apa_without_doi_uses_pubmed():
    paper = PubMedPaper(
        pmid="999",
        title="A title",
        authors=[],
        journal="J",
        year="",
        volume="",
        issue="",
        pages="",
        doi="",
        abstract="",
        pub_types=[],
    )
    out = format_apa_journal_article(paper)
    assert "https://pubmed.ncbi.nlm.nih.gov/999/" in out
