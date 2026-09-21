# RIGHTS.ORG.NZ — API Routes

from fastapi import APIRouter, UploadFile, File
from core.ocr import ocr_image, OCR_MODULE_READY
from core.pdf import pdf_to_images, PDF_MODULE_READY
from core.boot import boot_check
import time

router = APIRouter()

# OCR endpoint
@router.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = ocr_image(image_bytes)
    return {"text": text}


# PDF endpoint
@router.post("/pdf")
async def pdf_endpoint(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    images = pdf_to_images(pdf_bytes)

    results = []
    for img in images:
        text = ocr_image(img)
        results.append(text)

    return {"pages": results}


# Info endpoint
START_TIME = time.time()

@router.get("/info")
async def info():
    uptime = round(time.time() - START_TIME, 2)

    return {
        "system": "RIGHTS.ORG.NZ Backend",
        "version": "1.0.0",
        "modules": {
            "OCR": OCR_MODULE_READY,
            "PDF": PDF_MODULE_READY
        },
        "uptime_seconds": uptime,
        "status": "online"
    }


# Status (health-check)
@router.get("/status")
async def status():
    return {"status": "ok"}


# Boot check
@router.get("/boot")
async def boot():
    return boot_check()
