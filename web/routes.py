from fastapi import APIRouter, UploadFile, File
from core.ocr import ocr_image
from core.pdf import pdf_to_images

router = APIRouter()

@router.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = ocr_image(image_bytes)
    return {"text": text}

@router.post("/pdf")
async def pdf_endpoint(file: UploadFile = File(...)):
    # Read PDF bytes
    pdf_bytes = await file.read()

    # Convert PDF to images
    images = pdf_to_images(pdf_bytes)

    # Run OCR on each page
    results = []
    for img in images:
        text = ocr_image(img)
        results.append(text)

    return {"pages": results}
