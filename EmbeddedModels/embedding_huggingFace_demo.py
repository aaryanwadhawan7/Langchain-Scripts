## We can use inference API and for local machine as well !
## HuggingFaceEmbeddings requires sentence-transformers to generate embeddings!
## pip install sentence-transformers

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv ()

embedding = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')

text = 'Cristiano Ronaldo is the best Portugal football player of all time.'

result = embedding.embed_query(text)

print (str(result))