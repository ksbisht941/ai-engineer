from dotenv import load_dotenv
load_dotenv()  # must run before any LangChain import so LangSmith env vars are picked up

from fastapi import FastAPI
from pydantic import BaseModel

from app.chain import build_chain

app = FastAPI()
chat_chain = build_chain()

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = chat_chain.invoke(
        {"input": req.message},
        config={"configurable": {"session_id": req.session_id}}
    )

    return ChatResponse(response=result.content)