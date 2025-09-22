from pydantic import BaseModel

class DocumentTypeCreate(BaseModel):
    name: str

class DocumentTypeOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
