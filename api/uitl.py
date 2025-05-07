from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],bcrypt__rounds=15,deprecated="auto")

def hashing(password:str):

    return pwd_context.hash(password)

def verify(plain_password,loged_password):

    return pwd_context.verify(plain_password,loged_password)

