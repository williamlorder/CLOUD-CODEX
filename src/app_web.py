from __future__ import annotations

import tempfile
from pathlib import Path


def main() -> None:
    try:
        import streamlit as st
    except ImportError:
        raise RuntimeError("Install optional dependency: pip install .[web]")

    from src.app_cli import run_pipeline

    st.title("PubMed Citation Annotator")
    provider = st.selectbox("Provider", ["openai", "gemini"])
    k = st.slider("References (k)", min_value=5, max_value=10, value=8)
    email = st.text_input("NCBI email", value="you@example.com")
    text = st.text_area("Input text (English/Chinese)", height=240)

    if st.button("Run") and text.strip():
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write(text)
            temp_path = f.name
        class A:  # lightweight namespace
            pass
        a = A()
        a.provider = provider
        a.k = k
        a.input_file = temp_path
        a.outdir = "outputs"
        a.email = email
        a.config = None
        paths = run_pipeline(a)
        for name, path in paths.items():
            st.write(f"{name}: {Path(path)}")


if __name__ == "__main__":
    main()
