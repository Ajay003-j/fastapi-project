from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],bcrypt__rounds=15,deprecated="auto")

def hashing(password:str) ->str:

   hashed_pass = pwd_context.hash(password)
   return hashed_pass

def verify_pass(plain_password,hash_password) ->bool:

   return pwd_context.verify(plain_password,hash_password)
   