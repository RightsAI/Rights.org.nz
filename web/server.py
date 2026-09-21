# RIGHTS.ORG.NZ — FastAPI Web Server

from fastapi import FastAPI
from core.boot import boot_system
from web.routes import router

app = FastAPI()

@app.get("/status")
def system_status():
    return {"status": boot_system()}

# Register routes
app.include_router(router)

# Server ready flag
WEB_SERVER_READY = True
