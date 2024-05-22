from models import response
from JWT.JWTBearer import JWTBearer
from payment.infrastructure import payment_infra
from payment.models.payment_model import PaymentForm
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/{PaymentForm}")
async def payment(request: PaymentForm = Depends()):
    return await payment_infra.payment(request)

