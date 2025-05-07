from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Book(BaseModel):

    title:str
    author:str
    genre:str
    year:int

class Resuser(BaseModel):

    author:str
    class Config():
        orm_mode = True

class User(BaseModel):

    user_name:str
    email:EmailStr
    phone_no:Optional[str] = Field(max_length=10)
    password:str = Field(min_length=8)

class Username(BaseModel):

    user_name:str
    email:EmailStr

    class Config():
        orm_mode = True

class Token(BaseModel):

    acces_token : str
    token_type : str

class Tokendata(BaseModel):

    id : str