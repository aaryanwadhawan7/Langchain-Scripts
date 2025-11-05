from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv ()

## No need to mention the task as HuggingFaceEndpoint works with model that supports text generation!
## If you face any issue while running this script file download all the packages again 
## either by 'pip install -r requirements.txt' or 'pip install --user -r requirements.txt'

HFEndPt = HuggingFaceEndpoint (
    repo_id = 'deepseek-ai/DeepSeek-V3.2-Exp',
    max_new_tokens = 200,
    huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
)

model = ChatHuggingFace (llm = HFEndPt)

result = model.invoke ('Is Cristiano Ronaldo is the greatest player on planet earth ?')

print (result.content)