from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


class RetrievalService:

    DB_PATH = "./chroma_db"

    @staticmethod
    def search_keyword(keyword: str):

        vectordb = Chroma(
            persist_directory=RetrievalService.DB_PATH,
            embedding_function=HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        )

        docs = vectordb.similarity_search(keyword, k=5)

        return [
            {
                "content": doc.page_content,
                "source": doc.metadata
            }
            for doc in docs
        ]