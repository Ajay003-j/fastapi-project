from jose import jwt,JWTError
import secrets
from datetime import datetime,timedelta

secret_key = secrets.token_hex(32)
algorithm = "HS256"
expiriation_time = 30

def create_access_token(data:dict):

    to_encode = data.copy()
    expries = datetime.utcnow() + timedelta(minutes=expiriation_time)
    to_encode.update({"exp":expries})
    jwt_token = jwt.encode(to_encode,secret_key,algorithm=algorithm)
    return jwt_token