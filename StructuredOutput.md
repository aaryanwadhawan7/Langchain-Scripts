### Why do we need structured output ?

- Data Extraction
- API Building
- Agents (TOOLS NEED STRUCTURED OUTPUT)

### Ways to get structured output ?

- LLMs

  - 1. LLMs that can generate structured o/p on their own
  - with_strctured_output ()
  - Data Format -> TypedDict, Pydantic and json_schema

  - 2. LLMs that can't generate structured o/p on their own
  - Output parsers

### Pydantic Handbook

- Custom Validation : Field (IT CAN BE COMPLEX! WE CAN USE Annotated INSTEAD)

```python
from pydantic import BaseModel, Union, Optional, Field

## Schema

class person (BaseModel):
  first_name: str
  middle_name: Union[str, None]

  ## If we won't declare middle_name then it won't be any problem
  ## since we have passed None inside Union

  last_name: str
  address: Optional[str]

  ## Pydantic will ask user for address even it's an empty string

  username: str = "Username not defined yet!"
  sports: List[str] = []

  ## Generally, if you defined list like this then it will create a single one for all the instances
  ## Defined like this

  achievements: list = Field(default_factory = list)

## Nested

class detailInfo (BaseModel):
  userInfo : person
  phoneNo : int


user = person(first_name = "Aaryan", last_name = "Wadhawan", address = "", )
```
