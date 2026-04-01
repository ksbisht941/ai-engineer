from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    encode_kwargs={"normalize_embeddings": False},
)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_database",
)

result = vectorstore.similarity_search("How python use in data analysis?", k=1)

for r in result:
    print('page_content: ', r.page_content)
    print('metadata: ', r.metadata)

retriver = vectorstore.as_retriever()

docs = retriver.invoke("Where Neural networks used?")

for d in docs:
    print(d.page_content)