# RIGHTS.ORG.NZ — PDF Module

from pdf2image import convert_from_bytes
import io

# Convert PDF bytes to list of image bytes
def pdf_to_images(pdf_bytes):
    try:
        # Convert PDF to PIL images
        pil_images = convert_from_bytes(pdf_bytes)

        # Convert each PIL image to raw bytes
        image_bytes_list = []
        for img in pil_images:
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            image_bytes_list.append(buf.getvalue())

        return image_bytes_list

    except Exception as e:
        return [f"[PDF ERROR] {e}"]

# Module status
PDF_MODULE_READY = True
