from sqlalchemy.orm import Session
from app.models.event import Event


def processed(
    db: Session,
    event_id: str
):

    return (
        db.query(Event)
        .filter(Event.event_id == event_id)
        .first()
        is not None
    )
