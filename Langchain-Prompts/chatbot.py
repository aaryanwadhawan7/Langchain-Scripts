from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import os

load_dotenv ()

HFEndPt = HuggingFaceEndpoint (
    repo_id = 'deepseek-ai/DeepSeek-R1',
    max_new_tokens = 200,
    temperature = 1.2,
    huggingfacehub_api_token = os.getenv ('HUGGINGFACEHUB_API_TOKEN')
)

chatHistory = [
    SystemMessage (content = "Hi Deepseek!")
]

model = ChatHuggingFace(llm = HFEndPt)

while True:
    user_query = input('You: ')
    chatHistory.append(HumanMessage(content = user_query))
    if user_query == "exit":
        break
    result = model.invoke(chatHistory)
    print (f"AI: {result.content}")
    chatHistory.append(AIMessage(content = result.content))

print (chatHistory)
