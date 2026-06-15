from fastapi import FastAPI
from app.routes.webhook import router as webhook_router

app = FastAPI(
    title="Ledger Allocation Engine",
    version="1.0.0",
    description="Event-Driven Ledger Allocation Service"
)

app.include_router(webhook_router)

@app.get("/")
def health():
    return {"status": "Ledger Allocation Engine running..."}