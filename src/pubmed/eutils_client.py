from __future__ import annotations

import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Any

import requests

from src.utils.cache import DiskCache


@dataclass
class PubMedPaper:
    pmid: str
    title: str
    authors: list[str]
    journal: str
    year: str
    volume: str
    issue: str
    pages: str
    doi: str
    abstract: str
    pub_types: list[str]


class EUtilsClient:
    BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    def __init__(self, email: str, tool: str = "cloud-codex-citer", requests_per_sec: float = 3.0, cache: DiskCache | None = None) -> None:
        self.email = email
        self.tool = tool
        self.min_interval = 1.0 / requests_per_sec
        self.last_call = 0.0
        self.cache = cache or DiskCache()

    def _throttle(self) -> None:
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()

    def _get(self, endpoint: str, params: dict[str, Any], retries: int = 4) -> dict[str, Any] | str:
        key = f"{endpoint}:{sorted(params.items())}"
        cached = self.cache.get("pubmed", key)
        if cached is not None:
            return cached
        params = {**params, "email": self.email, "tool": self.tool}
        delay = 1.0
        for i in range(retries):
            try:
                self._throttle()
                resp = requests.get(f"{self.BASE}/{endpoint}", params=params, timeout=60)
                resp.raise_for_status()
                out: dict[str, Any] | str
                if params.get("retmode") == "json":
                    out = resp.json()
                else:
                    out = resp.text
                self.cache.set("pubmed", key, out)
                return out
            except requests.RequestException:
                if i == retries - 1:
                    raise
                time.sleep(delay)
                delay *= 2
        raise RuntimeError("unreachable")

    def esearch(self, query: str, retmax: int = 100) -> list[str]:
        data = self._get(
            "esearch.fcgi",
            {"db": "pubmed", "term": query, "retmax": retmax, "retmode": "json"},
        )
        assert isinstance(data, dict)
        return data.get("esearchresult", {}).get("idlist", [])

    def efetch(self, pmids: list[str]) -> list[PubMedPaper]:
        if not pmids:
            return []
        xml_text = self._get(
            "efetch.fcgi",
            {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"},
        )
        assert isinstance(xml_text, str)
        return self._parse_efetch(xml_text)

    def _parse_efetch(self, xml_text: str) -> list[PubMedPaper]:
        root = ET.fromstring(xml_text)
        papers: list[PubMedPaper] = []
        for article in root.findall(".//PubmedArticle"):
            pmid = (article.findtext(".//PMID") or "").strip()
            title = (article.findtext(".//ArticleTitle") or "").strip()
            journal = (article.findtext(".//Journal/Title") or "").strip()
            year = (article.findtext(".//PubDate/Year") or article.findtext(".//ArticleDate/Year") or "").strip()
            volume = (article.findtext(".//JournalIssue/Volume") or "").strip()
            issue = (article.findtext(".//JournalIssue/Issue") or "").strip()
            pages = (article.findtext(".//Pagination/MedlinePgn") or "").strip()
            abstract = " ".join(t.strip() for t in article.findall(".//Abstract/AbstractText") if t.text).strip()
            authors: list[str] = []
            for a in article.findall(".//AuthorList/Author"):
                last = (a.findtext("LastName") or "").strip()
                ini = (a.findtext("Initials") or "").strip()
                coll = (a.findtext("CollectiveName") or "").strip()
                name = coll or " ".join(p for p in [last, ini] if p)
                if name:
                    authors.append(name)
            doi = ""
            for aid in article.findall(".//ArticleId"):
                if aid.get("IdType") == "doi" and aid.text:
                    doi = aid.text.strip()
            pub_types = [pt.text.strip() for pt in article.findall(".//PublicationType") if pt.text]
            if pmid:
                papers.append(PubMedPaper(pmid, title, authors, journal, year, volume, issue, pages, doi, abstract, pub_types))
        return papers
