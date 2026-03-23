from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun(max_results=5)  # Limit results to avoid rate limits

results = search_tool.invoke("top news in india today")
print(results)
