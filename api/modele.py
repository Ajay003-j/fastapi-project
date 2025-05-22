from sqlalchemy import String,Column,Integer,DateTime,ForeignKey
from .dependancy import Base
from datetime import datetime

class ToDo(Base):
    __tablename__ = "to_do"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,nullable=False,index=True)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False,index=True)
    phone_number = Column(String,nullable=False,index=True)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False,index=True)
    content = Column(String,nullable=False,index=True)
    posted_at = Column(DateTime,nullable=True,default=datetime.utcnow)
    owner_id = Column(Integer,ForeignKey("to_do.id",ondelete="CASCADE"),nullable=False)