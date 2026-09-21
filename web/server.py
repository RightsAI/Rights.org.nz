# RIGHTS.ORG.NZ — Main Server

from fastapi import FastAPI
from web.routes import router

app = FastAPI(
    title="RIGHTS.ORG.NZ Backend",
    version="1.0.0",
    description="Backend API for OCR, PDF processing, and system info."
)

# Подключаем маршруты
app.include_router(router)


@app.get("/")
async def root():
    return {
        "system": "RIGHTS.ORG.NZ Backend",
        "message": "API is online",
        "docs": "/docs"
    }
