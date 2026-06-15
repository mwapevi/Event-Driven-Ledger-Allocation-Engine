from sqlalchemy import *
from app.db.base import Base
from datetime import datetime

class Allocation(Base):
    __tablename__ = "allocations"

    id = Column(Integer, primary_key=True)
    event_id = Column(String, nullable=False)
    bucket = Column(String, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    transfer_id = Column(UUID(as_uuid=True))
    status = Column(String)
    created_at = Column(DateTime)

