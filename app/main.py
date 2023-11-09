from fastapi import FastAPI
from .routers import auth_router

app = FastAPI()

app.include_router(auth_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Aquí puedes incluir más configuraciones, como middleware, CORS, etc.
