from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(expression: str) -> float:
    """Evaluate a math expression. Use for arithmetic."""
    return eval(expression)  # Use safe evaluator in prod

@tool("database_query")  # Custom name
def query_db(sql: str) -> str:
    """Execute SQL query on customer database."""
    # DB logic here
    return f"Results for: {sql}"



model = ChatMistralAI(model="open-mistral-nemo")
tools = [calculator, query_db]

model_with_tools = model.bind_tools(tools)

# LLM decides which tool to call
result = model_with_tools.invoke("Calculate 25*4 and query users from California")
print(result.tool_calls)