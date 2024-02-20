from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4

from app.database.models.user import User
from app.schemas.user import UserBase, UserCreate
from app.server import get_connection

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/")
async def create_user(
    data: UserCreate,
    db=Depends(get_connection),
) -> UserBase:
    return db.create(User, data)


@router.get("/{id}")
async def read_user(
    id: UUID4,
    db=Depends(get_connection),
) -> UserBase:
    if user := db.get_one(User, id):
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/")
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db=Depends(get_connection),
) -> list[UserBase]:
    return db.get_many(User, skip, limit)


@router.delete("/{id}")
async def delete_user(
    id: UUID4,
    db=Depends(get_connection),
) -> UserBase:
    if user := db.delete(User, id):
        return user
    raise HTTPException(status_code=404, detail="User not found")
