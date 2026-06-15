from sqlalchemy import *

from app.db.base import Base

class AllocationRule(Base):

    __tablename__ = "allocation_rules"

    id = Column(Integer, primary_key=True)

    bucket_name = Column(String)

    percentage = Column(Float)

    account_id = Column(String)