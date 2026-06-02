from fastapi import APIRouter
from pydantic import BaseModel
import chromadb
import re

router = APIRouter()

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("documents")


class QueryRequest(BaseModel):
    question: str


def clean_key(question: str):
    return question.lower().replace("what is", "").replace("?", "").strip()


def extract_value(text: str, field: str):
    patterns = [
        rf"{field}\s*[:\-]?\s*([^\n]+)",
        rf"{field}\s+([^\n]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return None


@router.post("/query")
def query_document(request: QueryRequest):

    results = collection.query(
        query_texts=[request.question],
        n_results=3
    )

    chunks = results["documents"][0]
    context = "\n".join(chunks)

    field = clean_key(request.question)

    value = extract_value(context, field)

    if value:
        return {
            "question": request.question,
            "answer": value
        }

    return {
        "question": request.question,
        "relevant_chunks": chunks
    }