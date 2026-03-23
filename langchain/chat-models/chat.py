from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq

# model = init_chat_model("gpt-4.1")
model = ChatGroq(model="llama-3.3-70b-versatile", max_tokens=20)

response = model.invoke("write a poem on AI")

print(response.content)