from __future__ import annotations


def han_ratio(text: str) -> float:
    if not text:
        return 0.0
    han_chars = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
    return han_chars / max(1, len(text))


def is_chinese_text(text: str, threshold: float = 0.08) -> bool:
    """Heuristic Chinese detection via Han character ratio."""
    return han_ratio(text) >= threshold
