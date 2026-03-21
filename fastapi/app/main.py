"""
Main entry point for the FastAPI application.
"""
from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Initialize the FastAPI app
app = FastAPI(title="FastAPI v2")

# Create database tables on startup
Base.metadata.create_all(bind=engine)

# Include the API routes
app.include_router(router)


@app.get("/")
def root():
    """
    Root endpoint to verify the API is running.
    """
    return {"message": "API with DB is running"}