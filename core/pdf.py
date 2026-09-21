# RIGHTS.ORG.NZ — PDF Module

from pdf2image import convert_from_bytes
import io

def pdf_to_images(pdf_bytes):
    try:
        pil_images = convert_from_bytes(pdf_bytes)

        image_bytes_list = []
        for img in pil_images:
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            image_bytes_list.append(buf.getvalue())

        return image_bytes_list

    except Exception as e:
        # Возвращаем список с одной ошибкой, чтобы не ломать цикл
        return [f"[PDF ERROR] {e}"]


PDF_MODULE_READY = True
