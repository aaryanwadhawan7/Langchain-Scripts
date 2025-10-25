from langchain_community.document_loaders import PyPDFLoader
from pypdf import PdfReader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv ()

llm = GoogleGenerativeAI(model = 'gemini-2.5-pro')

'''
reader = PdfReader('Python_Topics.pdf')

print (reader.is_encrypted)
'''

loader = PyPDFLoader(
    file_path = 'Python_Topics.pdf',
    password = None
)

prompt = PromptTemplate(
    template = 'Give the topic of the following: \n {text}',
    input_variables = ['text']
)

docs = loader.load()

## print (len(docs))
## print (docs[0].page_content)
## print (docs[0].metadata)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({'text' : docs[0]})
## print (result)
## print (type (docs))

print (type (docs[0]))
## <class 'langchain_core.documents.base.Document'>