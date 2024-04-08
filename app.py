# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from UserItem.router import userRouter

app = FastAPI()

# Agrega las rutas de la API
app.include_router(userRouter.router, prefix="/user")

# Lista de orígenes permitidos
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

# Agrega el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



