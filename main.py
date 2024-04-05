# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from UserItem.controller import user_controller
from UserItem.models import user_model

app = FastAPI()

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

# Aquí estamos definiendo las rutas de nuestra API
@app.get("/items/{item_id}", response_model=user_model.Item)
def read_item(item_id: int):
    return user_controller.get_item(item_id)

@app.get("/items/", response_model=list[user_model.Item])
def read_items():
    return user_controller.get_items()

@app.post("/items/", response_model=user_model.Item)
def create_item(item: user_model.Item):
    return user_controller.create_item(item)

