from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from hermanitto_docs_api.models.base import Base


class DocumentType(Base):
    __tablename__ = "document_types"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
