from __future__ import annotations

import re
from typing import List

EN_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'\(])")
ZH_SENTENCE_RE = re.compile(r"(?<=[。！？；!?])")


def split_english_sentences(text: str) -> List[str]:
    text = text.strip()
    if not text:
        return []
    parts = [p.strip() for p in EN_SENTENCE_RE.split(text) if p.strip()]
    return parts


def split_chinese_sentences(text: str) -> List[str]:
    text = text.strip()
    if not text:
        return []
    parts = [p.strip() for p in ZH_SENTENCE_RE.split(text) if p.strip()]
    return parts


def split_sentences(text: str, chinese: bool) -> List[str]:
    return split_chinese_sentences(text) if chinese else split_english_sentences(text)
