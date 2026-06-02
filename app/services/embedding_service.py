import chromadb


class EmbeddingService:

    @staticmethod
    def chunk_text(text, chunk_size=1000, overlap=200):

        chunks = []
        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])

            if end >= len(text):
                break

            start = end - overlap

        return chunks

    @staticmethod
    def create_vector_store(text, filename):

        chroma_client = chromadb.PersistentClient(path="./chroma_db")

        collection = chroma_client.get_or_create_collection("documents")

        chunks = EmbeddingService.chunk_text(text)

        collection.add(
            ids=[f"{filename}_{i}" for i in range(len(chunks))],
            documents=chunks,
            metadatas=[{"source": filename} for _ in chunks]
        )

        return len(chunks)