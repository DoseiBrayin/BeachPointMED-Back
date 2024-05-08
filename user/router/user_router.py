from fastapi import APIRouter, Depends
from models import response
from JWT.JWTBearer import JWTBearer
from user.infrastructure import user_infrastructure as user
from user.model.user_response import UserResponse

router = APIRouter()

@router.post("/", response_model=response.APIResponse, dependencies=[Depends(JWTBearer())])
def create_user(user_data: UserResponse ):
    return user.create_user(user_data)