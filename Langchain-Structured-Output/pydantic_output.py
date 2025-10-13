## Generate structured output with validation via pydantic module 
from pydantic import BaseModel, Field
from typing import Annotated, Union
import json

# Define the schema
class Review(BaseModel):
    user_id: int
    product_id: int
    content: str
    pros: str = Field(..., min_length=50)
    cons: Union[str, None] = Field(None, min_length=50)
    review_summary: Annotated[str, "Positive or Negative or Neutral Review!"]

# Corrected review data
user_review = {
    'user_id': 121002,
    'product_id': 5412,
    'content': 'Samsung-S23 is a top segment smartphone from Samsung, providing great day-to-day performance, smooth multi-tasking, and reliability for daily use.',
    'pros': 'Camera quality is excellent even in challenging lighting situations, the phone design is comfortable and modern, and the performance remains smooth throughout most tasks.',
    'cons': 'Battery life could be improved for heavy users, and the device tends to get warm during extended gaming sessions.',
    'review_summary': 'Positive'
}


## Validation and output

## output = Review(**user_review)
## output_dict = dict(output)
## print(output_dict['review_summary'])

user_review = Review(**user_review)
user_review_json = user_review.model_dump_json()
user_review_dict = json.loads(user_review_json)
print (user_review_dict['cons'])