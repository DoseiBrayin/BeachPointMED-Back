from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models import response
from locations.infrastructure import location_infrastructure

router = APIRouter()

# Aquí estamos definiendo las rutas de nuestra API REST
@router.get("/locations/", response_model=response.APIResponse) 
def read_locations():
    return location_infrastructure.get_locations()