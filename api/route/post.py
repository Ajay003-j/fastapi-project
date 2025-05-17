from fastapi import APIRouter,HTTPException,Depends,status
from api import dependancy,modele
from api.schema import New_post
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/')
async def create_posts(new_post:New_post,db:Session = Depends(dependancy.get_db)):

    created_post = modele.Post(**new_post.model_dump())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post