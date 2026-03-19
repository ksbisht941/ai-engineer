# from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("document_loader/GRU.pdf")
documents = loader.load()

print(documents)

template = ChatPromptTemplate.from_messages(
    [("system", "you are a AI that summarize the text"), ("human", "{data}")]
)

model = ChatMistralAI(model="mistral-small-2506")

prompt = template.format_messages(data=documents[0].page_content)

response = model.invoke(prompt)

print(response.content)
