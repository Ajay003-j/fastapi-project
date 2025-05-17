from pydantic import BaseModel,Field,EmailStr
from typing import Optional
from datetime import datetime

class New_user(BaseModel):  

    email : EmailStr
    password : str = Field(min_length=8)
    phone_number : str = Field(max_length=10)

class New_post(BaseModel):

    title : str
    content : str
    posted_at : str

