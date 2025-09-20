# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    age: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True # SQLAlchemy 모델 ↔ Pydantic 변환 허용
