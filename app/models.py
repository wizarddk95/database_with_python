# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    # MySql에서 autoincrement는 기본 값이 True
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

