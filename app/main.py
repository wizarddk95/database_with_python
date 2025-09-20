# app/main.py
from fastapi import FastAPI
from app.routers import users
from app.database import Base, engine

app = FastAPI()

# 라우터 등록
app.include_router(users.router)
