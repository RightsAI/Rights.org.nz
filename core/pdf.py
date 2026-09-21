# RIGHTS.ORG.NZ — PDF Processing Module

from pdf2image import convert_from_path
from core.ocr import extract_text

# Convert PDF to images and extract text
def process_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path)
        full_text = ""

        for page in pages:
            page_path = "temp_page.png"
            page.save(page_path, "PNG")
            text = extract_text(page_path)
            full_text += text + "\n"

        return full_text

    except Exception as e:
        return f"[PDF ERROR] {e}"

# Module status
PDF_MODULE_READY = True
