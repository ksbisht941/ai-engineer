from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import os

# Load environment variables
load_dotenv()

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

print("Rag system created (CLI Mode)")
print("Press 0 to exit")

while True:
    query = input("You: ")
    if query == "0":
        break
    
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })
    
    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")
    