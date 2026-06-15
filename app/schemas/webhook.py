from pydantic import BaseModel
from datetime import datetime

class ColumnWebhook(BaseModel):
    event_type: str
    event_id: str
    amount: float
    account_id: str
    timestamp: datetime


#class DepositWebhook(BaseModel):
  #  event_type: str
   # event_id: str
   # amount: float
   # account_id: str
   # timestamp: datetime

class DepositWebhook(BaseModel):
    amount: float
    source: str