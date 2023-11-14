
from app.db.database import Base
from sqlalchemy import Column,Integer,String ,DateTime 
from datetime import datetime 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String )
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True )
    created = Column(DateTime, default=datetime.now, onupdate=datetime.now )