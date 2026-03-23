# from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langchain.agents import create_agent, AgentState
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
import requests
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

@tool
def get_exchange_rate(from_currency: str, to_currency: str, amount: Optional[float] = 1.0) -> str:
    """Get the real-time exchange rate from `from_currency` to `to_currency`.
    
    Use ISO 4217 currency codes (USD, EUR, GBP, etc.).
    Optionally specify `amount` to convert a specific value.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rate = data['rates'].get(to_currency)
        if rate is None:
            return f"Error: {to_currency} not supported for {from_currency}"
        
        if amount == 1.0:
            return f"1 {from_currency} = {rate:.4f} {to_currency}"
        else:
            converted = amount * rate
            return f"{amount} {from_currency} = {converted:.2f} {to_currency} (rate: 1 {from_currency} = {rate:.4f} {to_currency})"
    except Exception as e:
        return f"Error fetching rate: {str(e)}"

# Initialize model and agent
model = ChatMistralAI(model="open-mistral-nemo", temperature=0)
tools = [get_exchange_rate]

checkpointer = MemorySaver()  # Enables conversation memory
agent = create_agent(
    model,
    tools,
    checkpointer=checkpointer,
    system_prompt="You are a currency exchange assistant. Use the tool for all rate queries. Provide clear, formatted answers."
)

# Example usage with memory (same thread_id maintains conversation)
config = {"configurable": {"thread_id": "currency-chat"}}

# # First query
# result1 = agent.invoke(
#     {"messages": [HumanMessage(content="What's the USD to EUR rate?")]},
#     config
# )
# print(result1["messages"][-1].content)


for chunk in agent.stream(
    {"messages": [HumanMessage(content="Convert 500 GBP to JPY")]}, 
    config,
    stream_mode="values"
):
    if "messages" in chunk:
        last_msg = chunk["messages"][-1]
        if hasattr(last_msg, "content") and last_msg.content:
            print(last_msg.content, end="", flush=True)