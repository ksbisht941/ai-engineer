# Chatbot API

This is a basic FastAPI application that wraps the LangChain-based chatbot.

## Setup

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    Ensure you have a `.env` file in the root directory (or in this folder) with the necessary API keys:
    - `GOOGLE_API_KEY`
    - `MISTRAL_API_KEY`

3.  **Run the application**:
    ```bash
    # If standard uvicorn command works:
    uvicorn api:app --reload

    # If 'uvicorn' command is not found, use python module:
    python -m uvicorn api:app --reload
    ```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Streaming API (Experimental)

I have also added a streaming version of the API in `stream_api.py`.

1.  **Run the streaming server**:
    ```bash
    python -m uvicorn stream_api:app --reload --port 8001
    ```

2.  **Test streaming with curl**:
    ```bash
    curl -N -X POST "http://127.0.0.1:8001/stream_chat" \
         -H "Content-Type: application/json" \
         -d '{"query": "What is deep learning?"}'
    ```
    *(The `-N` flag tells curl not to buffer the output, so you see tokens as they arrive.)*

## Endpoints Summary

| File | Endpoint | Type | Description |
| :--- | :--- | :--- | :--- |
| `api.py` | `/chat` | Buffered | Waits for full response, returns JSON. |
| `stream_api.py` | `/stream_chat` | Streaming | Streams tokens one by one as they are generated. |
