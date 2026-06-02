import os
from fastapi import APIRouter, UploadFile, File

from app.services.ocr_service import OCRService
from app.services.embedding_service import EmbeddingService

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # OCR extraction
    text = OCRService.extract_text(file_path)

    # Store in ChromaDB
    chunks_count = EmbeddingService.create_vector_store(text, file.filename)

    return {
        "filename": file.filename,
        "text_length": len(text),
        "chunks": chunks_count
    }