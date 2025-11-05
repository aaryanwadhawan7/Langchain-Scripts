from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv ()

embedding = HuggingFaceEmbeddings (model_name = 'all-MiniLM-L6-v2')

documents = [
    'Cristiano Ronaldo is the greatest player on planet earth',
    'Lionel Messi is considered to be greatest of all time.',
    'Neymar Jr is usually called prince who never got his crown.'
]

query = 'Tell me about Cristiano Ronaldo'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

## Always pass 2D List inside cosine_similarity
## print (cosine_similarity([query_embedding], doc_embedding))

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print (query)
print (documents[index])
print (f"similarity score is {score}")