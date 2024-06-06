from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from JWT import jwtmanager

class JWTBearer(HTTPBearer):
    async def __call__(self, request:Request):
        token = await super().__call__(request)
        if not jwtmanager.validate_token(token.credentials):
            raise HTTPException(status_code=403, detail="Invalid Token")
        return True