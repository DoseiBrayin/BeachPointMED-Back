from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from models import response
from timeCourts.infrastructure import timeCourts_infrastructure
from JWT.JWTBearer import JWTBearer


router = APIRouter()

# Aquí estamos definiendo las rutas de nuestra API REST
@router.get("/timeCourts/{location}", response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def read_timeCourts(location:str):
    return timeCourts_infrastructure.get_timeCourts(location)

@router.get("/timeCourts/{date}/{location}", response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def read_timeCourts_by_date(date:str,location:str):
    return timeCourts_infrastructure.get_timeCourts_by_date(date,location)
