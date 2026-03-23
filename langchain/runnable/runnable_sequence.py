from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate.from_template('Write a joke about {topic}')
model = ChatMistralAI()
parser = StrOutputParser()
prompt2 = PromptTemplate.from_template('Explain the following joke - {text}')

# Use pipe operator instead of RunnableSequence constructor
chain = prompt1 | model | parser | prompt2 | model | parser

print(chain.invoke({'topic': 'AI'}))