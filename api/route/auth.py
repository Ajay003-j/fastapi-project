from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api import modele,dependancy,utils,oauth

route = APIRouter(tags=["Authentication"])

@route.post('/login')
def login_user(user_credential:OAuth2PasswordRequestForm = Depends(),
               db:Session=Depends(dependancy.get_db)):

    user = db.query(modele.ToDo).filter(modele.ToDo.email == user_credential.username).first()

    if not user:

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="wrong credentials")
    
    if not utils.verify_pass(user_credential.password,user.password):

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="wrong credentials")
    
    token = oauth.create_access_token(data={"user_id":user.id})
    
    return {token:"bearer"}