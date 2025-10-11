from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv ()

HFEndPt = HuggingFaceEndpoint (
    repo_id = 'deepseek-ai/DeepSeek-R1',
    max_new_tokens = 200,
    temperature = 1.2,
    huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
)

model = ChatHuggingFace(llm = HFEndPt)

messages = [
    SystemMessage (content = "Hi, please help me some doubts!"),
    HumanMessage (content = "Give me study plan for learning Generative AI ?")
]

result = model.invoke (messages)
messages.append (AIMessage(content = result.content))

print (messages)