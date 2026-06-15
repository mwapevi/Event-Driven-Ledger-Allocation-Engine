from sqlalchemy import Column, String, Float, DateTime
from app.db.base import Base
import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, index=True)
    event_type = Column(String)
    raw_payload = Column(String)
    created_at = Column(DateTime)