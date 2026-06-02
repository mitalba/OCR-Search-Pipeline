# OCR Document Search System (FastAPI + ChromaDB)

This project allows you to:
- Upload PDF/Image documents
- Extract text using OCR
- Store embeddings in ChromaDB
- Search or query documents using keywords/questions

---

# ⚙️ Requirements

pip install -r requirements.txt

### Install Python 3.10+

---

# 📌 Install Tesseract OCR

## Windows:
Download:
https://github.com/UB-Mannheim/tesseract/wiki

Set path in code:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

## Linux:
sudo apt install tesseract-ocr

## Mac:
brew install tesseract

---

# 🚀 Run Server

uvicorn app.main:app --reload --port 8085

---

# 🌐 Open API Docs

http://127.0.0.1:8085/docs

---

# 📡 API Endpoints

---

## 📤 Upload Document

POST /upload

Upload PDF or image file.

### Response:
```json id="q1k9ld"
{
  "filename": "invoice.pdf",
  "text_length": 1200,
  "chunks": 5
}

🔍 Search Documents

GET /search?keyword=invoice

Response:
{
  "keyword": "invoice",
  "results": [
    "Invoice Number: 12345",
    "Total Amount: $500"
  ]
}
❓ Query Document (RAG-style)

POST /query

Request:
{
  "question": "What is invoice number?"
}
Response:
{
  "question": "What is invoice number?",
  "answer": "12345"
}

OR fallback:

{
  "relevant_chunks": ["...text..."]
}