import pdfplumber
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


# ⚠️ Windows path (change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRService:

    @staticmethod
    def extract_text(file_path: str) -> str:

        text = ""

        # PDF
        if file_path.endswith(".pdf"):

            try:
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
            except Exception:
                pass

            # fallback OCR
            if not text.strip():
                pages = convert_from_path(file_path)
                for page in pages:
                    text += pytesseract.image_to_string(page)

        # IMAGE
        else:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)

        return text