# RIGHTS.ORG.NZ — Boot Module

from core.ocr import OCR_MODULE_READY
from core.pdf import PDF_MODULE_READY

def boot_check():
    return {
        "OCR": OCR_MODULE_READY,
        "PDF": PDF_MODULE_READY,
        "system_ready": OCR_MODULE_READY and PDF_MODULE_READY
    }
