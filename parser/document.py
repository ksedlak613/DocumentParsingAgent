from pathlib import Path
from parser.llm import run_llm

def parse_document(file_path: str) -> str:
    text = Path(file_path).read_text(encoding="utf-8")
    return run_llm(f"Extract structured insights from this document:\n{text}")
