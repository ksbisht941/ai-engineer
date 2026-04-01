from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Chatbot API",
    description="A basic FastAPI wrapper for the LangChain-based chatbot.",
    version="1.0.0"
)

# Initialize LangChain components
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    encode_kwargs={"normalize_embeddings": False},
)

# Use absolute path for Chroma DB to ensure it's found when running from different locations
# Assuming the database is in the same folder as this script
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_database")

# Fallback to root chroma_database if not found in project folder
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

llm = ChatMistralAI(model="mistral-small-2506")

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

# Pydantic models for API request/response
class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

@app.get("/", tags=["Health"])
async def health_check():
    """Basic health check endpoint."""
    return {"status": "up", "message": "Chatbot API is running"}

@app.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(request: ChatRequest):
    """
    Takes a query and returns the AI response based on the document context.
    """
    try:
        query = request.query
        docs = retriever.invoke(query)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )
        
        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })
        
        response = llm.invoke(final_prompt)
        
        return ChatResponse(response=response.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
