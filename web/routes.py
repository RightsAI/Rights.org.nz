from fastapi import APIRouter, UploadFile, File
from core.ocr import ocr_image

router = APIRouter()

@router.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    # Read file bytes
    image_bytes = await file.read()

    # Run OCR
    text = ocr_image(image_bytes)

    return {"text": text}
