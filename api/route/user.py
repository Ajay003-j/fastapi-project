from fastapi import APIRouter, HTTPException,Depends,status
from api import validate
from api import modele,uitl
from api.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/users',tags=['users'])

@router.post('/',response_model=validate.Username,status_code=status.HTTP_201_CREATED)
async def create_data(new_user:validate.User,db:Session =Depends(get_db)):

    hashed_password = uitl.hashing(new_user.password)
    new_user.password = hashed_password

    create_user = modele.User(**new_user.dict())
    db.add(create_user)
    db.commit()
    db.refresh(create_user)

    return create_user

@router.get('/{id}',response_model=validate.Username)
async def get_user(id:int,db:Session=Depends(get_db)):
    
    user_data = db.query(modele.User).filter(modele.Db.id == id).first()

    if not user_data:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return user_data
