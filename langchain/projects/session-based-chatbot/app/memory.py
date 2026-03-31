# from langchain_community.chat_message_histories import ChatMessageHistory

# # In-memory store (replace with Redis in production)
# store = {}

# def get_session_history(session_id: str):
#     if session_id not in store:
#         store[session_id] = ChatMessageHistory()
#     return store[session_id]



import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

def get_session_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(session_id, url=REDIS_URL)