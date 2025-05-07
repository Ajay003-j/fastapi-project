from fastapi import APIRouter, HTTPException,Depends,status
import psycopg2.extras
from api import validate
import psycopg2
from api import modele,oauth2
from api.database import engine,get_db
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session

router = APIRouter(prefix='/books',tags=['books'])

@router.get('/')
async def get_data(db:Session = Depends(get_db)):

    data = db.query(modele.Db).all()

    return data

@router.post('/',response_model=validate.Resuser,status_code=status.HTTP_201_CREATED)
async def create_data(new_data:validate.Book,db:Session =Depends(get_db),
                      get_book:int = Depends(oauth2.verify_access_token)):

    create_data = modele.Db(**new_data.dict())

    db.add(create_data)
    db.commit()
    db.refresh(create_data)

    return create_data

@router.get('/{id}',response_model=validate.Resuser)
async def get(id:int,db:Session=Depends(get_db)):

    one_data=db.query(modele.Db).filter(modele.Db.id == id)
    One_Data = one_data.first()

    if not one_data:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return One_Data

@router.put('/{id}')
async def update_data(id :int,data:validate.Book,db:Session=Depends(get_db)):

    updated_data = db.query(modele.Db).filter(modele.Db.id == id)
    up_data=updated_data.first()

    if not up_data:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    updated_data.update(data.dict(),synchronize_session=False)
    db.commit()

    return updated_data.first()

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int,db:Session=Depends(get_db)):

    deleted_data=db.query(modele.Db).filter(modele.Db.id == id)
    data = deleted_data.first()

    if data == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    deleted_data.delete(synchronize_session=False)
    db.commit()

    return data
