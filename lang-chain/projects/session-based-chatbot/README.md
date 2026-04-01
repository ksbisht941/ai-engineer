# Session-Based Chatbot

A conversational chatbot built with **FastAPI**, **LangChain**, and **Mistral AI** that remembers chat history per user session using **Redis**.

---

## How It Works

### The Big Picture

```
User (HTTP POST /chat)
        │
        ▼
   FastAPI (main.py)
        │  session_id + message
        ▼
RunnableWithMessageHistory (chain.py)
        │
        ├──► Redis (memory.py)
        │    Loads past messages for this session_id
        │
        ▼
  ChatPromptTemplate
  [ system message ]
  [ history messages ]   ◄── injected from Redis
  [ new human message ]
        │
        ▼
  Mistral LLM (config.py)
        │
        ▼
  AI Response
        │
        ├──► Redis  (history saved back automatically)
        │
        ▼
  Return response to user
```

---

### Step-by-Step Flow

1. **User sends a request** to `POST /chat` with a `session_id` and `message`.

2. **FastAPI** receives it and calls `chat_chain.invoke()`, passing the `session_id` via config.

3. **`RunnableWithMessageHistory`** uses the `session_id` to call `get_session_history()`:
   - Fetches all previous messages for that session from **Redis**.
   - Injects them into the prompt as `history`.

4. **The prompt** is assembled in order:
   - `system` → sets the assistant's behavior.
   - `history` → all past human + AI messages for this session.
   - `human` → the new incoming message.

5. **Mistral LLM** receives the full prompt and generates a response.

6. **LangChain automatically saves** the new human message and AI response back to Redis.

7. **FastAPI returns** the AI response to the user.

---

### Why Sessions?

Each user gets a unique `session_id`. Redis stores their conversation history under that key, so:

- Different users never see each other's history.
- The same user gets a continuous conversation across multiple requests.
- History persists even if the server restarts.

---

## Project Structure

```
session-based-chatbot/
├── app/
│   ├── main.py       # FastAPI app, /chat endpoint
│   ├── chain.py      # LangChain prompt + LLM + memory chain
│   ├── config.py     # Mistral LLM setup
│   └── memory.py     # Redis session history
├── .env              # API keys and Redis URL
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Install dependencies
```bash
uv pip install -r requirements.txt
uv pip install redis
```

### 2. Start Redis

Choose one of the three options below:

---

#### Option A — Docker (recommended, no install needed)
```bash
# Pull and start Redis in the background
docker run -d --name redis-chatbot -p 6379:6379 redis

# Check it's running
docker ps

# Stop it when done
docker stop redis-chatbot

# Start it again later
docker start redis-chatbot
```

---

#### Option B — Homebrew (macOS)
```bash
# Install Redis
brew install redis

# Start Redis as a background service (auto-restarts on reboot)
brew services start redis

# Or run it manually in the foreground (stops when you close the terminal)
redis-server

# Stop the background service
brew services stop redis
```

---

#### Option C — Direct binary (Linux)
```bash
# Ubuntu / Debian
sudo apt update && sudo apt install redis-server

# Start the service
sudo systemctl start redis

# Enable auto-start on boot
sudo systemctl enable redis

# Stop it
sudo systemctl stop redis
```

---

#### Verify Redis is running

After starting with any option, confirm it's alive:
```bash
redis-cli ping
# Expected output: PONG
```

You can also inspect saved sessions:
```bash
redis-cli
> KEYS *                  # list all session keys
> LRANGE <key> 0 -1      # view messages in a session
> DEL <key>              # delete a session
```

### 3. Configure `.env`
```env
MISTRAL_API_KEY="your-mistral-api-key"
REDIS_URL="redis://localhost:6379"
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```

---

## API Usage

### `POST /chat`

**Request:**
```json
{
  "session_id": "user-123",
  "message": "What is the capital of France?"
}
```

**Response:**
```json
{
  "response": "The capital of France is Paris."
}
```

Send a follow-up in the same session — the bot remembers context:
```json
{
  "session_id": "user-123",
  "message": "What language do they speak there?"
}
```
```json
{
  "response": "They speak French in Paris."
}
```

---

## Redis Session Storage

| Feature | In-Memory | Redis |
|---|---|---|
| Survives server restart | ❌ | ✅ |
| Shared across workers | ❌ | ✅ |
| Auto-expiry (TTL) | ❌ | ✅ |

To set a TTL (auto-expire sessions after 1 hour), update `memory.py`:
```python
RedisChatMessageHistory(session_id, url=REDIS_URL, ttl=3600)
```

