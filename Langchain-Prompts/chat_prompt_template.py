## HumanMessage, AIMessage and SystemMessage
## ChatPromptTemplate -> List of Messages

from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate (
    [
        ("system", "Hi, hope I'll be helpfull with your {domain} project."),
        ("human", "Can you give me roadmap for learning {topic}")
    ]
)

prompt = template.invoke({'domain' : 'Generative AI', 'topic' : 'Langchain'})

print (prompt)