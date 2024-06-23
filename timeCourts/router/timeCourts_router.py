import uuid
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from models import response
from timeCourts.infrastructure import timeCourts_infrastructure
from JWT.JWTBearer import JWTBearer
from helpers.scheduler import scheduler_job
from fastapi import BackgroundTasks

router = APIRouter()

# Aquí estamos definiendo las rutas de nuestra API REST
@router.get("/timeCourts/{location}", response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def read_timeCourts(location:str):
    return timeCourts_infrastructure.get_timeCourts(location)

@router.get("/timeCourts/{date}/{location}", response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def read_timeCourts_by_date(date:str,location:str):
    return timeCourts_infrastructure.get_timeCourts_by_date(date,location)

@router.get("/Reserverd/{id}",response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def change_state(id:str, background_tasks: BackgroundTasks):
    id_list = [i for i in id.split(",")]
    task_id = str(uuid.uuid4())
    background_tasks.add_task(scheduler_job,timeCourts_infrastructure.change_status_available, 1,task_id, id_list)
    return timeCourts_infrastructure.change_status_reserved(id_list, task_id)

@router.get("/Available/{id}",response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def change_state(id:str):
    id_list = [i for i in id.split(",")]
    return timeCourts_infrastructure.change_status_available(id_list)

@router.get("/Unavalible/{id}",response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def change_state(id:str):
    id_list = [i for i in id.split(",")]
    return timeCourts_infrastructure.change_status_unavailable(id_list)