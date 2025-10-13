from typing import TypedDict, Optional, Annotated
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv ()

HFEndPt = HuggingFaceEndpoint (
    repo_id = 'deepseek-ai/DeepSeek-R1',
    huggingfacehub_api_token = os.getenv ('HUGGINGFACEHUB_API_TOKEN'),
    max_new_tokens = 100,
    temperature = 1.2
)

## NO VALIDATION
class person (TypedDict):
    name : str
    age : int
    email : Optional[str]
    RegNo : Optional[Annotated[str, 'NOT ASSIGNED YET!']]
    Incident : Annotated[str, 'Write the incident in detail ?']

'''
user : person = {'name' : 'Aaryan Wadhawan',
                 'age' : 22 }
'''

model = ChatHuggingFace (llm = HFEndPt)
structured_model = model.with_structured_output(person)

result = model.invoke('''Aaryan Wadhawan, 22yrs CAM at Real Madrid was playing against Barcelona in the Champions League final and it was 91st min when Lamine Yamal lost the ball 
                and it was an intense counter-attack when bellingham delivered the ball via outer foot of the boot
                to youngster and he kicked the ball inside the net with great strike! What a worlie kick!
                And with that he remembers his responsibilities and started writing Langchain-scripts!''')

dict_result = dict(result)
## print (dict_result)
print (dict_result['name'])