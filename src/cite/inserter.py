from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FootnoteAssignment:
    footnote_number: int
    pmid: str
    sentence_indices: list[int]


def insert_footnotes(sentences: list[str], assignments: list[FootnoteAssignment]) -> list[str]:
    sentence_to_markers: dict[int, list[int]] = {}
    for a in assignments:
        for idx in a.sentence_indices:
            sentence_to_markers.setdefault(idx, []).append(a.footnote_number)

    out: list[str] = []
    for i, sentence in enumerate(sentences):
        markers = sentence_to_markers.get(i, [])
        if markers:
            suffix = "".join(f"[^${m}]".replace("$", "") for m in sorted(set(markers)))
            out.append(f"{sentence.rstrip()} {suffix}".rstrip())
        else:
            out.append(sentence)
    return out
