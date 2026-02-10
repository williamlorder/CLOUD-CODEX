from src.utils.sentence_split import split_chinese_sentences, split_english_sentences


def test_split_english_sentences():
    text = "This is one sentence. This is two! Is this three?"
    assert split_english_sentences(text) == [
        "This is one sentence.",
        "This is two!",
        "Is this three?",
    ]


def test_split_chinese_sentences():
    text = "这是第一句。这是第二句！这是第三句？"
    assert split_chinese_sentences(text) == ["这是第一句。", "这是第二句！", "这是第三句？"]
