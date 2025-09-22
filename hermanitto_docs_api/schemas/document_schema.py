from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    type_id: int
    link: str

class DocumentOut(BaseModel):
    id: int
    type_id: int
    link: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
