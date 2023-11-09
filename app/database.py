from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER='dbuser'
PASSWD='admin123'
HOST='localhost'
DBNAME='fastapi'

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWD}@{HOST}/{DBNAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
