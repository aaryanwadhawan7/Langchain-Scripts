## Suppose, we are given a text on any topic, we have to generate the summary and small quiz on that topic parallel
## And after that merge both the chain to get one single o/p

## RunnableParallel -> Takes chain I/P and give chain as O/P

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Annotated, Optional
from langchain_core.runnables import RunnableParallel

load_dotenv ()

llm = GoogleGenerativeAI(model = 'gemini-2.5-pro')

parser = StrOutputParser()

## summary_prompt and quiz_prompt will form a chain completely independently with respect to each other!
summary_prompt = PromptTemplate(
    template = 'Write a small summary on the topic under 100 words: {topic}',
    input_variables = ['topic']
)

quiz_prompt = PromptTemplate(
    template = 'Genrate a small 5 question quiz on the topic: {topic}',
    input_variables = ['topic']
)

parallel_chain = RunnableParallel({
    'summary': summary_prompt | llm | parser,
    'quiz' : quiz_prompt | llm | parser
})

result = parallel_chain.invoke({'topic' : 'Machine Learning'})

## print (type(result))
parallel_chain.get_graph().print_ascii()