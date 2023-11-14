from fastapi import FastAPI 
import uvicorn 
from app.db.database import Base,engine
from app.routers import user,auth,web

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user.router)

app.include_router(auth.router)
app.include_router(web.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Las URLs de los frontend que permitirás
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)