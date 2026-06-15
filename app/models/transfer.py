from sqlalchemy import Column, Integer, String, Numeric, DateTime
from app.db.base import Base
import datetime

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True)
    event_id = Column(String, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    created_at = Column(DateTime)