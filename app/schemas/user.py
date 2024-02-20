from hashlib import sha256

from pydantic import UUID4, BaseModel, EmailStr, validator


class UserBase(BaseModel):
    id: UUID4
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

    @validator("password")
    def hash_password(cls, password: str):
        return sha256(password.encode()).hexdigest()
