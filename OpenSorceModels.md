### Open Source Models VS Closed Source Models

- Control

  - Can modify, finetune and deploy anywhere [OSMs]
  - Locked to provider's infrastructure [CSMs]

- Data Privacy

  - Runs locally [OSMs]
  - Sends queries to provider's servers [CSMs]

- Customization

  - Can fine-tune on specific datasets [OSMs]
  - No access to fine-tuning in most cases [CSMs]

- Deployement

  - Can be deployed on-premise servers or cloud
  - Must use vendor's API

#### HuggingFace : The largest repo of open-source LLMs

- We can use HuggingFace models via HuggingFace Inference API (1) and Local Machine (2)

- (1) dir : 2.ChatModels/chatModel_huggingFace_demo.py

```python
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",  # Known supported model
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

result = llm.invoke("Who is the most renowned personality of Portugal?")
print(result)
```

- (2) dir : 2.ChatModels/chatModel_huggingFace_local_demo.py

#### Embeddings

##### OpenAI

- Generating embeddings for a string

```python
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv ()

embeddings = OpenAIEmbeddings (model = 'text-embedding-3-small', dimensions = 100)

result = embeddings.embed_query ('What is the capital of Germany ?')

print (str(result))
```

- Generating embeddings for documents

```python
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv ()

embedding = OpenAIEmbeddings (model = 'text-embedding-3-small', dimensions = 100)

document = [
  "Who is the captain of current Real Madrid team ?",
  "Who is the captain of current Barcelona team ?",
  "Who is the captain of the current Juventus team ?"
]

result = embedding.embed_documents(document)
print (str(result))
```
