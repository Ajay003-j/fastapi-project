from fastapi import APIRouter,HTTPException,status,Depends
from .. import dependancy,schema,modele,utils,oauth
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_user(user:schema.New_user,db:Session = Depends(dependancy.get_db)):

    unreadable_text = utils.hashing(user.password)
    user.password = unreadable_text

    new_user = modele.ToDo(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user