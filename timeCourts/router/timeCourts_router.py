from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models import response
from timeCourts.infrastructure import timeCourts_infrastructure

router = APIRouter()

# Aquí estamos definiendo las rutas de nuestra API REST
@router.get("/timeCourts/{location}", response_model=response.APIResponse)
def read_timeCourts(location:str):
    return timeCourts_infrastructure.get_timeCourts(location)

@router.get("/timeCourts/{date}/{location}", response_model=response.APIResponse)
def read_timeCourts_by_date(date:str,location:str):
    return timeCourts_infrastructure.get_timeCourts_by_date(date,location)
