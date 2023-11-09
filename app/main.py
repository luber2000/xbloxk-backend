from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth_router


app = FastAPI()

app.include_router(auth_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Aquí puedes incluir más configuraciones, como middleware, CORS, etc.

# Configura el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Las URLs de los frontend que permitirás
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)
