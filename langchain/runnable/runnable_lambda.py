# from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate.from_template('Write a joke about {topic}')
model = ChatMistralAI()
parser = StrOutputParser()

# Pipe replaces RunnableSequence
joke_gen_chain = prompt | model | parser

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),          # Passes input (joke) unchanged
    'word_count': RunnableLambda(word_count)  # Wraps pure function
})

# Pipe chains the steps
final_chain = joke_gen_chain | parallel_chain

result = final_chain.invoke({'topic': 'AI'})
final_result = f"{result['joke']} \n word count - {result['word_count']}"

print(final_result)