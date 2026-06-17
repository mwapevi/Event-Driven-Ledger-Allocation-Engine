from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.webhook import ColumnWebhook, DepositWebhook
from app.services.event_processor import process_event
from app.db.session import SessionLocal

router = APIRouter(
    prefix="/webhook",
   # tags=["Webhook"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events")
def process_event_webhook(
    payload: ColumnWebhook,
    db: Session = Depends(get_db)
):
    return process_event(db, payload)

@router.post("/deposit")
def process_deposit_webhook(payload: DepositWebhook):
    return {
        "received": payload.amount,
        "source": payload.source
    }