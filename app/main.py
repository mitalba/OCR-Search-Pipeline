from fastapi import FastAPI
from app.routes import upload, query, search

app = FastAPI(title="OCR Search Pipeline")

app.include_router(upload.router)
app.include_router(query.router)
app.include_router(search.router)


@app.get("/")
def home():
    return {"message": "OCR pipeline is running"}