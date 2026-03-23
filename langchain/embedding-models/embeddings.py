from dotenv import load_dotenv

load_dotenv()

# from langchain_openai import OpenAIEmbeddings

# embeddings = OpenAIEmbeddings(
#     model = 'text-embedding-3-large',
#     dimensions=64
# )

# texts = [
#     "Hello this is Akarsh Vyas",
#     "Hello your name is YouTube",
#     "And you all are very beautiful"
# ]

# vector = embeddings.embed_documents(texts)

# print(vector)

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
)

# vector = embeddings.embed_query("What is product management?")
# print(len(vector))

docs = [
    "AI is transforming products",
    "Embeddings convert text into vectors"
]

vectors = embeddings.embed_documents(docs)

print(vectors)