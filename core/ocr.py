# RIGHTS.ORG.NZ — OCR Module

import pytesseract
from PIL import Image

# OCR main function
def extract_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"[OCR ERROR] {e}"

# Module status
OCR_MODULE_READY = True

import io

def ocr_image(image_bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"[OCR ERROR] {e}"
