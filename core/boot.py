# RIGHTS.ORG.NZ — System Boot Module

from core.init import SYSTEM_BOOT
from core.config import PROJECT_NAME, VERSION
from core.ocr import OCR_MODULE_READY
from core.pdf import PDF_MODULE_READY

# Boot sequence
def boot_system():
    status = []

    status.append(f"Booting {PROJECT_NAME} v{VERSION}...")
    status.append("Checking core system... OK" if SYSTEM_BOOT else "Core system failed")

    status.append("Checking OCR module... OK" if OCR_MODULE_READY else "OCR module failed")
    status.append("Checking PDF module... OK" if PDF_MODULE_READY else "PDF module failed")

    status.append("System is ready." if all([SYSTEM_BOOT, OCR_MODULE_READY, PDF_MODULE_READY]) else "System failed to start.")

    return "\n".join(status)

# Boot status
BOOT_MODULE_READY = True
