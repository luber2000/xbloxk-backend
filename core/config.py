import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY  = os.getenv('SECRET_KEY')
ALGORITHM  = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES  = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

class Settings:
  MYSQL_USER:str = os.getenv('MYSQL_USER')
  MYSQL_PASSWD:str = os.getenv('MYSQL_PASSWD')
  MYSQL_HOST:str = os.getenv('MYSQL_HOST')
  MYSQL_DBNAME:str = os.getenv('MYSQL_DBNAME')
  DATABASE_URL:str = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}/{MYSQL_DBNAME}'


settings = Settings