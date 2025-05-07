from api.database import Base
from sqlalchemy import Column,Integer,String

class Db(Base):

    __tablename__ = 'books'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False,index=True)
    author = Column(String,nullable=False,index=True)
    genre = Column(String,nullable=False,index=True)
    year = Column(Integer,nullable=False,index=True)

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String,nullable=False,index=True,unique=True)
    email = Column(String,nullable=False,index=True,unique=True)
    phone_no = Column(String,index=True,server_default='1234567890')
    password = Column(String,nullable=False,index=True)

