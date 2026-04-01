from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatMistralAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# Expected Output:
# A plain string containing a 5-line summary of the detailed report on black holes, e.g.:
#
# "Black holes are regions in space where gravity is so intense that nothing, not even light, can escape.
# They form when massive stars collapse under their own gravity at the end of their life cycle.
# The boundary of a black hole is called the event horizon, beyond which escape is impossible.
# At the center lies a singularity — a point of infinite density where known physics breaks down.
# Supermassive black holes, found at the centers of most galaxies, can be billions of times the mass of the Sun."