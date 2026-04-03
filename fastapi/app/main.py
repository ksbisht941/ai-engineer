"""
Main entry point for the FastAPI v3 Production application.
This file initializes the app and connects all the routers.
"""
from fastapi import FastAPI
from app.api.routes import router

# Initialize the FastAPI application
# In production, we give it a clear title and version
app = FastAPI(title="FastAPI v3 Production")

# Register the API routes under the app
# This allows us to separate route definitions into different files
app.include_router(router)


@app.get("/")
def root():
    """
    Root endpoint to verify that the API is up and running.
    """
    return {"message": "FastAPI v3 Production is running"}