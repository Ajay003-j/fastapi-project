
from sqlalchemy import Integer,Column,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine

database_url = 'postgresql+psycopg2://postgres:Ajay2004@localhost:5432/api_db'
engine = create_engine(database_url)

Base = declarative_base()


sessionlocal = sessionmaker(autoflush=False,bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db

    finally:
        db.close()
