import os
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from app.core.db_config import get_db
from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(
    title="Library Management System",
    description="API for managing library resources",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.mount("/", StaticFiles(directory="frontend/public", html=True), name="static")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Library Management System API"}
