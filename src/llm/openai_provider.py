from __future__ import annotations

import json
import os
from typing import Any

import requests

from src.llm.provider_base import Claim, LLMProvider, QueryBundle, RerankResult
from src.utils.cache import DiskCache


class OpenAIProvider(LLMProvider):
    def __init__(self, model: str = "gpt-4o-mini", base_url: str = "https://api.openai.com/v1", cache: DiskCache | None = None) -> None:
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY missing")
        self.cache = cache or DiskCache()

    def _chat_json(self, prompt: str) -> Any:
        key = f"{self.model}:{prompt}"
        cached = self.cache.get("openai", key)
        if cached is not None:
            return cached
        resp = requests.post(
            f"{self.base_url}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": "Return strict JSON only."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.2,
                "response_format": {"type": "json_object"},
            },
            timeout=60,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        self.cache.set("openai", key, parsed)
        return parsed

    def translate(self, sentences: list[str]) -> list[str]:
        prompt = (
            "Translate each sentence into formal academic English. Keep index alignment. "
            "Output JSON with key translations: list[str].\n"
            f"sentences={json.dumps(sentences, ensure_ascii=False)}"
        )
        data = self._chat_json(prompt)
        return data.get("translations", [])

    def extract_claims(self, text: str, sentence_count: int) -> list[Claim]:
        prompt = (
            "Extract 5-20 atomic scientific claims from text. Map each to sentence indices (0-based). "
            f"Sentence count: {sentence_count}. Output JSON {{claims:[{{claim:string,sentence_indices:number[]}}]}}.\n{text}"
        )
        data = self._chat_json(prompt)
        return [Claim(claim=c["claim"], sentence_indices=list(map(int, c.get("sentence_indices", [])))) for c in data.get("claims", [])]

    def generate_queries(self, text: str) -> QueryBundle:
        prompt = (
            "Generate 3-8 PubMed-ready Boolean queries, include MeSH terms when relevant. "
            "Also give concise baseline keyword query. Output JSON {queries:[], baseline_query:string}.\n"
            f"text={text}"
        )
        data = self._chat_json(prompt)
        return QueryBundle(queries=data.get("queries", []), baseline_query=data.get("baseline_query", ""))

    def rerank(self, text: str, claims: list[Claim], candidates: list[dict[str, Any]]) -> list[RerankResult]:
        prompt = (
            "Given claims and PubMed candidates, score each 0-1 for support and list supported claim indices. "
            "Prefer stronger evidence (reviews/meta-analyses). Output JSON {results:[{pmid,score,supported_claim_indices,rationale}]}.\n"
            f"claims={json.dumps([c.__dict__ for c in claims], ensure_ascii=False)}\n"
            f"candidates={json.dumps(candidates, ensure_ascii=False)}\n"
            f"context={text[:5000]}"
        )
        data = self._chat_json(prompt)
        results = []
        for r in data.get("results", []):
            results.append(
                RerankResult(
                    pmid=str(r.get("pmid", "")),
                    score=float(r.get("score", 0)),
                    supported_claim_indices=list(map(int, r.get("supported_claim_indices", []))),
                    rationale=r.get("rationale", ""),
                )
            )
        return results
