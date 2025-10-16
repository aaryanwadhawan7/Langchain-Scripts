from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv ()

llm = GoogleGenerativeAI (model = 'gemini-2.5-pro')

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me some random facts about {topic}. \n \n{format_instructions}',
    input_variables = ['topic'],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
    ## partial_variables : Definite, we need to pass everytime when we want to generate o/p via prompt
)

chain = template | llm | parser

result = chain.invoke ({'topic' : 'galaxy'})

print (type(result))
## <class 'dict'>

lst = result['galaxy_facts']
for l in lst:
    ## l -> dictionary
    print (f"{l['id']}: {l['fact']} \n")





