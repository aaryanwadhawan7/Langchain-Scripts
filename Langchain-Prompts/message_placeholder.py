from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

## Message Template
chat_template = ChatPromptTemplate([
    ('system', "Hi, I would like to help you with your project."),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human', '{query}')
]
)

chat_history = []
## Load the chat
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print (chat_history)

## Create a prompt
prompt = chat_template.invoke ({'chat_history': chat_history, 'query':"How do i process with my project ?"})
print (prompt)