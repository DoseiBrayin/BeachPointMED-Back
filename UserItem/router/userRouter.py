from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from UserItem.infrastructure import user_infrastructure
from UserItem.models import user_model
from models import response

router = APIRouter()

# Aquí estamos definiendo las rutas de nuestra API REST
@router.get("/items/{item_id}", response_model=user_model.Item)
def read_item(item_id: int):
    return user_infrastructure.get_item(item_id)

@router.get("/items/", response_model=response.APIResponse)
def read_items():
    return user_infrastructure.get_items()

@router.post("/items/", response_model=user_model.Item)
def create_item(item: user_model.Item):
    return user_infrastructure.create_item(item)