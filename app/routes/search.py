from fastapi import APIRouter
import chromadb

router = APIRouter()

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("documents")


@router.get("/search")
def search(keyword: str):

    results = collection.query(
        query_texts=[keyword],
        n_results=5
    )

    return {
        "keyword": keyword,
        "results": results["documents"][0]
    }