from openai import OpenAI
from parser.llm import run_llm

client = OpenAI()

def parse_audio(file_path: str) -> str:
    transcript = client.audio.transcriptions.create(
        file=open(file_path, "rb"),
        model="whisper-1"
    )
    return run_llm(f"Summarize and extract key points:\n{transcript.text}")
