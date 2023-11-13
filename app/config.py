import os

if os.path.exists('.env'):
  from dotenv import load_dotenv
  load_dotenv()

USER = os.getenv('USER')
PASSWD = os.getenv('PASSWD')
HOST = os.getenv('HOST')
DBNAME = os.getenv('DBNAME')


SECRET_KEY  = os.getenv('SECRET_KEY')
ALGORITHM  = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES  = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
