from models import response
from JWT.JWTBearer import JWTBearer
from products.infrastructure import products_infrasctructure
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

router = APIRouter()
#, dependencies=[Depends(JWTBearer())]
@router.get("/", response_model=response.APIResponse)
def read_products():
    return products_infrasctructure.get_Allproducts()