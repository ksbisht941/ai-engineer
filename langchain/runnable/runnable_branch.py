# from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate.from_template('Write a short report on {topic}')
prompt2 = PromptTemplate.from_template('Summarize the following text \n {text}')
model = ChatMistralAI()
parser = StrOutputParser()

# Generate report first
report_gen_chain = prompt1 | model | parser

# Conditional function (replaces RunnableBranch)
def should_summarize(text: str) -> str:
    """Returns 'summarize' if >300 words, else passes text through."""
    if len(text.split()) > 300:
        return prompt2 | model | parser
    return RunnablePassthrough()

# Pipe chains with conditional routing
final_chain = report_gen_chain | should_summarize

print(final_chain.invoke({'topic': 'Russia vs Ukraine'}))