from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db_config import get_db
import os
from sqlalchemy.sql import text

app = FastAPI(
    title="Library Management System",
    description="API for managing library resources",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Library Management System API"}

@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        # Test database connection
        await db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "environment": os.getenv("ENV", "development")
        }
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}