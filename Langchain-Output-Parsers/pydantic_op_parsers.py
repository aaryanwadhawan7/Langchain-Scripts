from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from typing import Annotated, Union, Optional
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv ()

## Pydantic Schema
## Let's generate a information card for the greatest ever sports person on planet earth

llm = GoogleGenerativeAI(model = 'gemini-2.5-pro')

class sportsPerson (BaseModel):
    name: str
    age: int
    sports: str
    nationality: Annotated[str, "What is the nationality of the sports person?"]
    titles: list[str]
    record: Optional[str]

## Parser will be responsible for validating the llm output
parser = PydanticOutputParser(pydantic_object = sportsPerson)


template = PromptTemplate(
    template = 'Generate a information card for the greatest ever sports person on planet earth? \n \n {format_instructions}',
    input_variables = [],
    partial_variables = {'format_instructions': parser.get_format_instructions}
)

chain = template | llm | parser

result = chain.invoke({})

print (result)
