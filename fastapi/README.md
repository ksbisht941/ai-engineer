# FastAPI CRUD Project

A simple and well-documented FastAPI project demonstrating CRUD (Create, Read, Update, Delete) operations using SQLAlchemy for database management and Pydantic for data validation.

## Project Structure

The core logic of the application is located in the `app/` directory:

- `main.py`: The entry point of the FastAPI application. It initializes the app, creates database tables, and includes the API routes.
- `database.py`: Handles database connection configuration and session management using SQLAlchemy.
- `models.py`: Defines the SQLAlchemy database models (the database schema).
- `schemas.py`: Contains Pydantic models for data validation and response formatting.
- `crud.py`: Contains the logic for database operations (Create, Read, Delete).
- `routes.py`: Defines the API endpoints and connects them to the CRUD operations.

## Project Flow

1.  **Request**: A client sends an HTTP request to an API endpoint (e.g., `POST /items`).
2.  **Routing**: `main.py` receives the request and routes it to the appropriate handler in `routes.py`.
3.  **Validation**: The request data is validated against the Pydantic schemas defined in `schemas.py`.
4.  **Database Session**: The `get_db` dependency in `database.py` provides a database session for the request.
5.  **CRUD Operation**: the route handler calls a function in `crud.py` to perform the requested operation.
6.  **Model Interaction**: The CRUD function uses SQLAlchemy models from `models.py` to interact with the database.
7.  **Response**: The result of the operation is formatted according to the response schema in `schemas.py` and returned to the client as a JSON response.

## Key Features

- **Root Endpoint**: Verify the API is running at `/`.
- **Create Item**: Add new items to the database via `POST /items`.
- **Read Items**: Retrieve all items via `GET /items` or a specific item by ID via `GET /items/{item_id}`.
- **Delete Item**: Remove an item by ID via `DELETE /items/{item_id}`.

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL database

### Installation

1.  Clone the repository and navigate to the project root.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Update the `DATABASE_URL` in `app/database.py` with your PostgreSQL credentials:
```python
DATABASE_URL = "postgresql://user:password@localhost:5432/fastapi_db"
```
*(Note: For `asyncpg`, you might need to use `postgresql+asyncpg://`)*

### Running the Application

Start the development server using Uvicorn:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
