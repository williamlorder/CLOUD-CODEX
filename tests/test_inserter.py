from src.cite.inserter import FootnoteAssignment, insert_footnotes


def test_insert_footnotes_reuses_indices():
    sents = ["A.", "B.", "C."]
    assignments = [
        FootnoteAssignment(1, "1", [0, 2]),
        FootnoteAssignment(2, "2", [2]),
    ]
    out = insert_footnotes(sents, assignments)
    assert out[0].endswith("[^1]")
    assert out[2].endswith("[^1][^2]")
