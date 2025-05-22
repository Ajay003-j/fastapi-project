from fastapi import APIRouter,Depends
from api import dependancy,modele,oauth
from api import schema
from sqlalchemy.orm import Session


router = APIRouter()

@router.post('/')
async def create_posts(new_post:schema.New_post,db:Session = Depends(dependancy.get_db),user_id:int=Depends(oauth.get_current_user)):

    created_post = modele.Post(owner_id = user_id.id,**new_post.model_dump())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post

@router.get('/',response_model=schema.Posts)
async def get_all_posts(db:Session = Depends(dependancy.get_db)):

    all_posts = db.query(modele.Post).all()
    return {"posts" : all_posts}
