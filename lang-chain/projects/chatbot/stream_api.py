from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import os

# Load environment variablesØ
load_dotenv()

app = FastAPI(
    title="Chatbot Streaming API",
    description="A FastAPI wrapper with streaming support for the LangChain-based chatbot.",
    version="1.0.0"
)

# Initialize LangChain components
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    encode_kwargs={"normalize_embeddings": False},
)

# Use absolute path for Chroma DB
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_database")
if not os.path.exists(CHROMA_PATH):
    CHROMA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../chroma_database"))

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

llm = ChatMistralAI(model="mistral-small-2506", streaming=True)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

class ChatRequest(BaseModel):
    query: str

async def generate_response(query: str):
    """
    Generator function to stream LLM tokens.
    """
    try:
        # 1. Retrieve relevant docs
        docs = await asyncio.to_thread(retriever.invoke, query)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })
        
        # 2. Stream tokens from the LLM
        async for chunk in llm.astream(final_prompt):
            yield chunk.content

    except Exception as e:
        # In a real-world app, you might want to log this error
        # Yielding a JSON-formatted error chunk can be helpful for the frontend
        yield json.dumps({"error": "Internal Server Error", "detail": str(e)})

@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "up", "message": "Streaming API is running"}

@app.post("/stream_chat", tags=["Chat"])
async def stream_chat(request: ChatRequest):
    """
    Returns a StreamingResponse that yields tokens as they are generated.
    """
    try:
        # We ensure the query is not empty
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
            
        return StreamingResponse(
            generate_response(request.query),
            media_type="text/plain"
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
