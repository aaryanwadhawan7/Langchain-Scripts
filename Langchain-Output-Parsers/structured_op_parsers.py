from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = GoogleGenerativeAI(model = 'gemini-2.5-pro')

## schema 
## Suppose we want to generate a short story about a fictional character
schema = [
    ResponseSchema(name = 'character_name', description = 'Write the name of fictional character.'),
    ResponseSchema(name = 'event_description', description = 'Give me 30 words description of the event.'),
    ResponseSchema(name = 'event_time', description = 'Give me detail about the time at which the event occured.')
]

parser = StructuredOutputParser.from_response_schemas(schema)

prompt = PromptTemplate(
    template = 'Generate a short story about a fictional character. \n \n {format_instructions}',
    input_variables = [],
    partial_variables = {'format_instructions' : parser.get_format_instructions}
)

chain = prompt | llm | parser

result = chain.invoke({})

print (result)