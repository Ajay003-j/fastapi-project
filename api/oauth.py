from jose import jwt,JWTError
import secrets
from datetime import datetime,timedelta
from fastapi import HTTPException,status,Depends
from api import schema
from fastapi.security import OAuth2PasswordBearer

oauth_schema = OAuth2PasswordBearer(tokenUrl='posts')

secret_key = secrets.token_hex(32)
algorithm = "HS256"
expiriation_time = 30

def create_access_token(data:dict):

    to_encode = data.copy()
    expries = datetime.utcnow() + timedelta(minutes=expiriation_time)
    to_encode.update({"exp":expries})
    jwt_token = jwt.encode(to_encode,secret_key,algorithm=algorithm)
    return jwt_token

def verify_token(token:str,credential_execption):
    try:
            
        data = jwt.decode(token,secret_key,algorithms=algorithm)
        id:str = data.get("user_id")

        if id is None:

            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you don't have access")
        token_data = schema.TokenData(id=id)
    except JWTError:
        raise credential_execption
    return token_data
    
def get_current_user(token = Depends(oauth_schema)):

    credential_execption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="you don't have access",
                                         headers={"WWW-Authenticate":"Bearer"})
    return verify_token(token,credential_execption)
