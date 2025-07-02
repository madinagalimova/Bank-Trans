from pydantic import BaseModel, Field
from datetime import datetime

class Transaction(BaseModel):
    id: str
    amount: float
    currency: str = Field(..., min_length=3, max_length=3)
    timestamp: datetime

    class Config:
        extra = 'allow'
