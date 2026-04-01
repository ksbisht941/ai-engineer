# from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate.from_template('Generate a tweet about {topic}')
prompt2 = PromptTemplate.from_template('Generate a Linkedin post about {topic}')
model = ChatMistralAI()
parser = StrOutputParser()

# Use pipe operator for sequences, dict for RunnableParallel
parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,      # Pipe replaces RunnableSequence
    'linkedin': prompt2 | model | parser    # Pipe replaces RunnableSequence
})

result = parallel_chain.invoke({'topic': 'AI'})
print(result['tweet'])
print(result['linkedin'])