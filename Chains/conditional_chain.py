from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch
## Runnable Lambda -> wrap any python callable 

load_dotenv()

## os.environ('GOOGLE_API_KEY') = os.getenv('GOOGLE_API_KEY')

llm = GoogleGenerativeAI(
    model = 'gemini-2.5-pro'
)

parser = StrOutputParser()

summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text under 50 words:\n\n{text}"
)
extend_prompt = PromptTemplate(
    input_variables=["text"],
    template="Extend the idea and real-world use case of this topic under 50 words:\n\n{text}"
)

summary_chain = summary_prompt | llm | parser
extend_chain = extend_prompt | llm | parser

## input -> text_input
def is_long_enough (input : dict) -> bool:
    return len(input["text"].split()) > 50

conditional_chain = RunnableBranch(
    (lambda x: is_long_enough(x), summary_chain),
    ## is_long_enough(text_input)
    extend_chain
)

text_input = {
    'text' : 'How is deep learning based on machine learning concepts!'
}

result = conditional_chain.invoke(text_input)

print (result)
conditional_chain.get_graph().print_ascii()

