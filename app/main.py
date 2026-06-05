from fastapi import FastAPI
from app.routes.webhook import router

app = FastAPI(
    title="Event Driven Ledger Allocation Engine"
)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "healthy"}
