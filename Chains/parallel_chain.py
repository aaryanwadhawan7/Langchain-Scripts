## Suppose, we are given a text on any topic, we have to generate the summary and small quiz on that topic parallel
## And after that merge both the chain to get one single o/p

## RunnableParallel -> Takes chain I/P and give chain as O/P

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Annotated, Optional

load_dotenv ()

llm = GoogleGenerativeAI(model = 'gemini-2.5-pro')

