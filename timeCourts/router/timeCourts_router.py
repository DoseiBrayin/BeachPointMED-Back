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

@router.get("/Reserverd/{id}",response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def change_state(id:str):
    return timeCourts_infrastructure.change_status_reserved(id)

@router.get("/Available/{id}",response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def change_state(id:str):
    return timeCourts_infrastructure.change_status_available(id)

@router.get("/Unavalible/{id}",response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def change_state(id:str):
    return timeCourts_infrastructure.change_status_unavailable(id)