from __future__ import annotations

import json
import os
from typing import Any

import requests

from src.llm.provider_base import Claim, LLMProvider, QueryBundle, RerankResult
from src.utils.cache import DiskCache


class GeminiProvider(LLMProvider):
    def __init__(self, model: str = "gemini-1.5-flash", cache: DiskCache | None = None) -> None:
        self.model = model
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY missing")
        self.cache = cache or DiskCache()

    def _json_call(self, prompt: str) -> Any:
        key = f"{self.model}:{prompt}"
        cached = self.cache.get("gemini", key)
        if cached is not None:
            return cached
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        payload = {
            "contents": [{"parts": [{"text": f"Return strict JSON only. {prompt}"}]}],
            "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"},
        }
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        parsed = json.loads(text)
        self.cache.set("gemini", key, parsed)
        return parsed

    def translate(self, sentences: list[str]) -> list[str]:
        data = self._json_call(
            "Translate each sentence into formal academic English while preserving index alignment. "
            f"Output {{translations:string[]}}. sentences={json.dumps(sentences, ensure_ascii=False)}"
        )
        return data.get("translations", [])

    def extract_claims(self, text: str, sentence_count: int) -> list[Claim]:
        data = self._json_call(
            "Extract 5-20 atomic claims from text with sentence indices (0-based). "
            f"Sentence count={sentence_count}. Output {{claims:[{{claim,sentence_indices}}]}}. text={text}"
        )
        return [Claim(claim=c["claim"], sentence_indices=list(map(int, c.get("sentence_indices", [])))) for c in data.get("claims", [])]

    def generate_queries(self, text: str) -> QueryBundle:
        data = self._json_call(
            "Generate 3-8 PubMed boolean queries + one concise baseline query. "
            f"Output {{queries:[], baseline_query:string}}. text={text}"
        )
        return QueryBundle(queries=data.get("queries", []), baseline_query=data.get("baseline_query", ""))

    def rerank(self, text: str, claims: list[Claim], candidates: list[dict[str, Any]]) -> list[RerankResult]:
        data = self._json_call(
            "Score each candidate 0-1 for claim support, include supported claim indices, rationale. "
            "Output {results:[{pmid,score,supported_claim_indices,rationale}]}. "
            f"claims={json.dumps([c.__dict__ for c in claims], ensure_ascii=False)} candidates={json.dumps(candidates, ensure_ascii=False)} context={text[:5000]}"
        )
        return [
            RerankResult(
                pmid=str(r.get("pmid", "")),
                score=float(r.get("score", 0)),
                supported_claim_indices=list(map(int, r.get("supported_claim_indices", []))),
                rationale=r.get("rationale", ""),
            )
            for r in data.get("results", [])
        ]
