## TypedDict -> No Validation 

from typing import TypedDict

class person (TypedDict):
    name: str
    age: int

person1 : person = {'name' : 'Aaryan Wadhawan', 'age': '22'}

print (person1)