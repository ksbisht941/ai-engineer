# from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate.from_template('Write a joke about {topic}')
model = ChatMistralAI()
parser = StrOutputParser()
prompt2 = PromptTemplate.from_template('Explain the following joke - {text}')

# Pipe operator replaces RunnableSequence
joke_gen_chain = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),                      # Passes input through unchanged
    'explanation': prompt2 | model | parser              # Pipe replaces RunnableSequence
})

# Pipe chains the steps
final_chain = joke_gen_chain | parallel_chain

print(final_chain.invoke({'topic': 'cricket'}))