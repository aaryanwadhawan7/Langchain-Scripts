from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st
import os 

load_dotenv()

HFEndPt = HuggingFaceEndpoint(
    repo_id = 'deepseek-ai/DeepSeek-V3.2-Exp',
    max_new_tokens = 200,
    temperature = 1.2,
    huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
)

model = ChatHuggingFace(llm = HFEndPt)

st.header ('Research Assistant')

paper_input = st.selectbox("Select Research Paper Name", [ "Attention Is All You Need", 
                                                          "BERT: Pre-training of Deep Bidirectional Transformers", 
                                                          "GPT-3: Language Models are Few-Shot Learners", 
                                                          "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explaination)"])

## Template 
template = load_prompt('template.json')

if st.button ('Summarize'):
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
    })
    st.write(result.content)