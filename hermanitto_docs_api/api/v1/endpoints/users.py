from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from hermanitto_docs_api.schemas.user_schema import UserCreate, UserOut
from hermanitto_docs_api.services.user_service import (
    create_user,
    authenticate_user,
    get_user_by_username,
)
from hermanitto_docs_api.core.dependencies import get_db
from hermanitto_docs_api.core.security import create_access_token, get_current_user

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)


@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
async def get_me(
    username: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
