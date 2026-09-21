# RIGHTS.ORG.NZ — Main Server

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from web.routes import router

app = FastAPI(
    title="RIGHTS.ORG.NZ Backend",
    version="1.0.0",
    description="Backend API for OCR, PDF processing, and system info."
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "system": "RIGHTS.ORG.NZ Backend",
        "message": "API is online",
        "docs": "/docs"
    }


@app.get("/test")
async def test_page():
    with open("web/test.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.get("/upload")
async def upload_page():
    with open("web/upload.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())
