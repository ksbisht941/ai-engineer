from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",     
    temperature=0.1                  
)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})
print(result)

# Expected Output:
# A Python dictionary parsed from the model's JSON response, e.g.:
# {
#     'facts': [
#         'Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape.',
#         'They form when massive stars collapse at the end of their life cycle.',
#         'The boundary surrounding a black hole is called the event horizon.',
#         'At the center of a black hole lies a singularity — a point of infinite density.',
#         'Supermassive black holes, millions to billions of times the mass of the Sun, exist at the centers of most galaxies.'
#     ]
# }