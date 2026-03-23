from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool
from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv

load_dotenv()

class CalcInput(BaseModel):
    a: float = Field(description="First number")
    b: float = Field(description="Second number")
    operation: str = Field(description="Operator: add, subtract, multiply, divide")

def calculator_logic(inputs: CalcInput) -> float:
    a, b, op = inputs.a, inputs.b, inputs.operation
    if op == "add": return a + b
    if op == "subtract": return a - b
    if op == "multiply": return a * b
    if op == "divide": return a / b
    raise ValueError("Invalid operation")

calculator_tool = StructuredTool.from_function(
    func=calculator_logic,
    name="advanced_calculator",
    description="Perform math operations with validation.",
    args_schema=CalcInput,
)


model = ChatMistralAI()
tools = [calculator_tool]

model_with_tools = model.bind_tools(tools)

# LLM decides which tool to call
result = model_with_tools.invoke("Search weather and calculate 25*4")
print(result)