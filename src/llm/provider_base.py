from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class Claim:
    claim: str
    sentence_indices: list[int]


@dataclass
class QueryBundle:
    queries: list[str]
    baseline_query: str


@dataclass
class RerankResult:
    pmid: str
    score: float
    supported_claim_indices: list[int]
    rationale: str


class LLMProvider(ABC):
    @abstractmethod
    def translate(self, sentences: list[str]) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def extract_claims(self, text: str, sentence_count: int) -> list[Claim]:
        raise NotImplementedError

    @abstractmethod
    def generate_queries(self, text: str) -> QueryBundle:
        raise NotImplementedError

    @abstractmethod
    def rerank(
        self,
        text: str,
        claims: list[Claim],
        candidates: list[dict[str, Any]],
    ) -> list[RerankResult]:
        raise NotImplementedError
