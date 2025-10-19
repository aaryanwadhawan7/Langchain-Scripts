from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Parses the dotenv file and load the environment variables
load_dotenv ()

model = GoogleGenerativeAI(model = 'gemini-2.5-pro')

parser = StrOutputParser ()

## Generate short report on facts about the Oppenheimer!
prompt = PromptTemplate(
    template = 'Generate short report on facts about the Oppenheimer.',
    input_variables = []
)

chain = prompt | model | parser

result = chain.invoke ({})

print (result)


