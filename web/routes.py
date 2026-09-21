# RIGHTS.ORG.NZ — API Routes

from fastapi import APIRouter, UploadFile, File
from core.ocr import extract_text
from core.pdf import process_pdf

router = APIRouter()

@router.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    filename = file.filename.lower()

    # Save uploaded file temporarily
    temp_path = "uploaded_file"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # PDF or image?
    if filename.endswith(".pdf"):
        text = process_pdf(temp_path)
    else:
        text = extract_text(temp_path)

    return {"text": text}
