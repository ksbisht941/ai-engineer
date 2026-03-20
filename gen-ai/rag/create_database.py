from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("documents/deep_learning.pdf")
documents = loader.load()

# print(documents)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = splitter.split_documents(documents)

# print(chunks)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    encode_kwargs={"normalize_embeddings": False},
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_database",
)

result = vectorstore.similarity_search("What is deep learning?", k=1)

for doc in result:
    print(doc.page_content)