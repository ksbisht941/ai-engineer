from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory

from app.config import get_llm
from app.memory import get_session_history

def build_chain():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer based on conversation context."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = (
        RunnablePassthrough()
        | prompt
        | llm
    )

    chain_with_memory = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    return chain_with_memory