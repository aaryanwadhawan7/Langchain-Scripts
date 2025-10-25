from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated, Optional

load_dotenv ()

url = 'https://docs.langchain.com/oss/python/langchain/knowledge-base#1-documents-and-document-loaders'

llm = GoogleGenerativeAI (model = 'gemini-2.5-pro')

class Guide (BaseModel):
    Pre_requisites : Annotated[str, 'List the pre-requisites developer must know before learning this tech.']
    Topics : list[str]
    Project_Ideas : Optional[list[str]] = Field(default = None, description = 'Suggest some project ideas related to this topic')

parser = PydanticOutputParser(pydantic_object = Guide)

loader = WebBaseLoader(url)

docs = loader.load()

data = docs[0].page_content

prompt = PromptTemplate(
    template = 'Examine the url and generate the output based on the following text: {text} \n {format_instructions}',
    input_variables = ['text'],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
)

chain = prompt | llm | parser

result = chain.invoke ({'text' : data})

print (result)