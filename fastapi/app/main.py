"""
Main entry point for the FastAPI v3 Production application.
"""
from fastapi import FastAPI
from app.api.routes import router

# Initialize the FastAPI app with production settings
app = FastAPI(title="FastAPI v3 Production")

# Include the API routes from the separated API layer
app.include_router(router)


@app.get("/")
def root():
    """
    Root endpoint to verify the API is running.
    """
    return {"message": "FastAPI v3 Production is running"}