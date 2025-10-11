## Static Prompt 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv ()

HFEndPt = HuggingFaceEndpoint(
    repo_id = 'deepseek-ai/DeepSeek-V3.2-Exp',
    max_new_tokens = 200,
    huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
)

model = ChatHuggingFace (llm = HFEndPt)

st.header ('Research Assistant')

user_input = st.text_input ('Enter your prompt ?')

if st.button ('Summarize'):
    result = model.invoke (user_input)
    st.write (result.content)