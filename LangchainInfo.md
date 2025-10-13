- Open anaconda prompt

  ```python
  conda activate C:\GenAI_env
  open .
  python -m venv venv
  venv\Scripts\Activate
  ```

  - These are all pay-as-you model as amount is defined on the basis number of token generation and API keys being used.

  ### LLMs (OpenAI)

  - General purpose model that are used for raw text generation. They take a string as I/p and returns a string.

  #### Implementation

  - visit platfrom.openai.com
  - Settings -> API Keys -> Create a new secret key
  - Create a .env file (OPENAI_API_KEY)
  - dir : 1.LLMs/1_llm_demo.py

  ```python
  from langchain_openai import OpenAI
  from dotenv import load_doatenv
  load_dotenv()

  llm = OpenAI(model='gpt-3.5-turbo-instruct')

  result = llm.invoke("What is the capital of India")

  ## print (result)
  print (result.content)
  ```

  ### Chat Models (OpenAI)

  - dir : 2.ChatModels/1_chatModel_openAPI.py

  ```python
  from langchain_openai import ChatOpenAI
  from dotenv import load_dotenv

  load_dotenv()
  model = ChatOpenAI(model='gpt-4', temperature = 0, max_completion_token = 10)

  '''
       Temperature is a parameter that controls the randomness of a language model's output.
       It affects how creative or deterministic the responses are:
       - Lower values (0.0 - 0.3) : More deterministic and predictable.
       - Higher values (0.7 - 1.5) : More random, creative and diverse.
  '''

  result = model.invoke ('What is the capital of India')

  print (result)
  ```

  ### Chat Models (Claude [Anthropic])

  - dir : 2.ChatModels/2_chatModel_claude.py

  - Go to console.anthropic.com
  - Go to API keys
  - Create a new API key
  - Copy the API key
  - Go to .env file (ANTHROPIC_API_KEY)

  ```python
  from langchain_anthropic import ChatAnthropic
  from dotenv import load_dotenv

  load_dotenv()

  chatModel = ChatAnthropic (model = 'claude-sonnet-4-5-20250929')

  result = chatModel.invoke('Name three places to visit in Germany?')

  print (result)
  ```

  ### Google Gemini ChatModel (See the implementation)

  - dir : 2.ChatModels/chatModel_gemini_demo.py

  ### List of Messages -> ChatPromptTemplate

  - dynamic : ChatPromptTemplate

  ### Message Placeholder

  - If we want to insert messages dynamically inside ChatPromptTemplate then we will use Message Placeholder
