from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import USER, PASSWD, HOST, DBNAME 

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWD}@{HOST}/{DBNAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
