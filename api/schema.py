from pydantic import BaseModel,Field,EmailStr
from typing import Optional
from datetime import datetime

class New_user(BaseModel): 
     
    username:str
    email : EmailStr
    password : str = Field(min_length=8)
    phone_number : str = Field(max_length=10)

class New_post(BaseModel):

    title : str
    content : str
    posted_at : str

class Posts(BaseModel):
    
    title : str
    content : str
    posted_at : str

    class Config():
        orm_mode = True

class TokenData(BaseModel):

    id :str

class Access_Token(BaseModel):

    token_data :str
    token_type :str

