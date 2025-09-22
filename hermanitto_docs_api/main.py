from fastapi import FastAPI
from hermanitto_docs_api.api.v1.endpoints import users, documents, types

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["documents"])
app.include_router(types.router, prefix="/api/v1/types", tags=["types"])
