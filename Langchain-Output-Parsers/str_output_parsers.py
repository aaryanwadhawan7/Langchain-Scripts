from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv ()

parser = StrOutputParser()

## Use TinyLlama/TinyLlama-1.1B-Chat-v1.0 model instead of current one
## Since TinyLlama can't produce structured output via with_structured_output()
model = GoogleGenerativeAI(model = 'gemini-2.5-pro')

'''
Task -> 1) Generate a report on a topic
2) Summarize the report that is generated
'''


## Step 1 : Report Prompt
report_prompt = PromptTemplate(
    template = 'Generate a short report on best {genre} movies of all time.',
    input_variables = ['genre']
)


## print (prompt1)
## text = 'Generate a short report on best thriller movies of all time.'


## Step 2 : Summary Prompt
summary_prompt = PromptTemplate(
    template = 'Generate the summary of the report : \n \n {report}',
    input_variables = ['report']
)


report_chain =  report_prompt | model | parser

summary_chain = {'report' : report_prompt} | summary_prompt | model | parser

result = summary_chain.invoke ({"genre" : "thriller"})

print (result)