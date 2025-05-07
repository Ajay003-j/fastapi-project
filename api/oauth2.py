from jose import JWTError,jwt
from datetime import timedelta,datetime
import secrets
from fastapi import HTTPException,Depends,status
from api import validate
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):

    to_encode = data.copy()
    exp = (datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).isoformate()
    to_encode.update({"expries":exp})

    Token = jwt.encode(to_encode,SECRET_KEY,algorithn=[ALGORITHM])
    return Token

def verify_access_token(token:str,credential_execption):

    try:

        payload = jwt.decode(token,SECRET_KEY,algorithm=[ALGORITHM])
        id : str = payload.get("user_id")
        
        if id is None:

            raise credential_execption

        token_data = validate.Tokendata(id=id)

    except JWTError:

        raise credential_execption
        
    return token_data 

def verify_credentials(token:str=Depends(oauth2_schema)):

    credential_execption = HTTPException(status_code = status.HTTP_404_NOT_FOUND,headers = {"www-Aurthiniticate":"Bearer"})
    return verify_access_token(token,credential_execption)
