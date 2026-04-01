from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatMistralAI(
    model="mistral-large-latest",    
    temperature=0.1                  
)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})
print(result)

# Expected Output:
# A Python dictionary with keys matching the defined schema, e.g.:
# {
#     'fact_1': 'Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape.',
#     'fact_2': 'They form when massive stars exhaust their fuel and collapse under their own gravity.',
#     'fact_3': 'The boundary surrounding a black hole is called the event horizon.'
# }