from fastapi import APIRouter,Depends,HTTPException,status,Response
from api import uitl,modele,database
from api import oauth2,validate
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['auth'])

@router.post('/login')
async def user_logs( user_cre:OAuth2PasswordRequestForm = Depends(),
    db:Session = Depends(database.get_db),user_id: int = Depends(oauth2.create_access_token)):

    user = db.query(modele.User).filter(modele.User.email == user_cre.username).first()

    if not user:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if not uitl.verify(user_cre.password,user.password):

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="wrong crendintials")
    
    access_token = oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token": access_token, "token_type": "bearer"}