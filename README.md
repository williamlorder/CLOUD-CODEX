# Cloud Codex Citation Annotator

Production-ready Python app that annotates academic text with PubMed-backed citations.

## Features

- English + Chinese input support.
- Chinese path: sentence-by-sentence translation to academic English while preserving sentence alignment.
- LLM-powered claim extraction, PubMed query expansion, and candidate reranking.
- PubMed retrieval via NCBI E-utilities (ESearch + EFetch), with:
  - `tool` + `email` compliance params
  - throttling (<=3 req/sec)
  - retry + exponential backoff
  - local disk cache for E-utilities and LLM calls
- Deterministic APA 7 formatting (no metadata hallucination).
- Markdown footnote insertion and full citation report.
- Machine-readable `citations.jsonl`.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
# optional tests
pip install -e .[test]
```

Set API keys via environment or `.env`:

```bash
OPENAI_API_KEY=...
GEMINI_API_KEY=...
```

## CLI

```bash
python -m src.app_cli --provider openai --k 8 --input-file input.txt --outdir outputs --email you@example.com
```

Stdin mode:

```bash
cat input.txt | python -m src.app_cli --provider gemini --k 10 --outdir outputs --email you@example.com
```

`--k` range is `1..50` (default 8). UI (optional Streamlit) exposes easy 5–10 slider.

## Optional config

Pass `--config config.json` or `--config config.yaml`.

Example JSON:

```json
{
  "llm": {
    "openai_model": "gpt-4o-mini",
    "openai_base_url": "https://api.openai.com/v1",
    "gemini_model": "gemini-1.5-flash"
  },
  "pubmed": {
    "tool": "cloud-codex-citer",
    "retmax": 80,
    "max_candidates": 200
  }
}
```

## Outputs

Each run creates `outputs/<timestamp>/`:

- `english_annotated.md`
- `original_annotated.md`
- `citation_report.md`
- `citations.jsonl`

## Architecture

- `src/app_cli.py`: main pipeline.
- `src/app_web.py`: optional Streamlit UI.
- `src/llm/*`: provider interface + OpenAI/Gemini implementations.
- `src/pubmed/*`: E-utilities client + ranking fusion.
- `src/cite/*`: APA formatting, footnote insertion, report/jsonl writing.
- `src/utils/*`: language detect, sentence splitting, cache.
- `tests/*`: unit tests for splitting, APA formatting, insertion.

## Notes on authority/safety

- Citations are only selected from PubMed records with PMIDs retrieved via E-utilities.
- No paper metadata is fabricated; missing fields are omitted.
- If initial retrieval is sparse, queries are automatically widened.

## Google Scholar

Google Scholar does not provide an official public API suitable for compliant production use. This app keeps PubMed as the authoritative source for biomedical/psych, and can be extended later with licensed scholarly APIs for social sciences.
