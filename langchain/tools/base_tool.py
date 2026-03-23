from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv

load_dotenv()

class SearchInput(BaseModel):
    query: str = Field(description="Search query")
    max_results: int = Field(default=5, description="Max results")

class CustomSearchTool(BaseTool):
    name: str = "custom_search"
    description: str = "Custom web search with rate limiting."
    args_schema: Type[BaseModel] = SearchInput

    def _run(
        self,
        query: str,
        max_results: int = 5,
        run_manager: CallbackManagerForToolRun | None = None,
    ) -> str:
        """Custom execution logic."""
        # Simulate API call with streaming
        if run_manager:
            run_manager.on_text("Searching...")
        # Real search logic
        return f"Top {max_results} results for '{query}'"

    # Optional async version
    async def _arun(self, query: str, **kwargs) -> str:
        return self._run(query, **kwargs)

search_tool = CustomSearchTool()

model = ChatMistralAI()
tools = [search_tool]

model_with_tools = model.bind_tools(tools)

# LLM decides which tool to call
result = model_with_tools.invoke("Search weather and calculate 25*4")
print(result.tool_calls)