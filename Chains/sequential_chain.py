from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from typing import Annotated, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

## Schema
class Scientist (BaseModel):
    name: str
    age: str
    achievements: list[str]
    projects: list[str]
    family: Optional[str] = Field(None, description = 'Give a 2 line description asbout the scientist family!')
    domain: str = Field('Give information about the domain in which the scientist has contributed!')

model = GoogleGenerativeAI(model = 'gemini-2.5-pro')

parser = PydanticOutputParser(pydantic_object = Scientist)

templateOne = PromptTemplate(
    template = 'Who led the greatest nuclear project in India ? \n \n {format_instructions}',
    input_variables = [],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
)


chainOne = templateOne | model | parser

text = chainOne.invoke({})

## Use this information and generate 5 pt summary of the above output
templateTwo = PromptTemplate(
    template = 'Generate the 5 pt summary about the following text: \n \n {text} \n \n {format_instructions}',
    input_variables = ['text'],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
)

chain = templateTwo | model | parser
chain.get_graph().print_ascii()

result = chain.invoke({'text' : text})

print (result)




