# FastAPI v3 Production-Grade Application

This is a production-ready FastAPI application with an asynchronous database layer, structured configuration, and database migrations.

## Project Structure (Production Layout)

```text
fastapi-app/
├── app/
│   ├── main.py              # Application entry point
│   ├── core/
│   │   ├── config.py        # Env-based settings (Pydantic)
│   │   └── database.py      # Async SQLAlchemy engine/session
│   ├── models/
│   │   └── item.py          # Database models
│   ├── schemas/
│   │   └── item.py          # Pydantic validation schemas
│   ├── crud/
│   │   └── item.py          # Async CRUD operations
│   ├── api/
│   │   └── routes.py        # API router and endpoints
│   └── dependencies.py      # Common dependencies
├── alembic/                 # Database migrations
├── alembic.ini              # Alembic configuration
├── .env                     # Environment variables
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## Key Improvements in v3

| Feature | Description |
| --- | --- |
| **Async Database** | Uses `SQLAlchemy` with `asyncpg` for non-blocking database operations. |
| **Alembic Migrations** | Robust database schema management with automated migrations. |
| **Structured Config** | Centralized environment-based configuration using `pydantic-settings`. |
| **Layered Architecture** | Clear separation of concerns between core, models, schemas, CRUD, and API layers. |
| **Connection Pooling** | Optimized database connection management for high performance. |

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL database
- `uv` (recommended) or `pip`

### Installation

1.  Clone the repository and navigate to the project root.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Create or update the `.env` file in the root directory:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/fastapi_db
```

### Database Migrations

Apply the initial database migrations to create the tables:
```bash
alembic upgrade head
```

### Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

## API Documentation

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Missing Features (Roadmap)

- Authentication (JWT, OAuth2)
- Rate Limiting
- Caching (Redis)
- Observability (Logging, Tracing)
- Background Jobs (Celery)
- Automated Tests (Unit, Integration)
