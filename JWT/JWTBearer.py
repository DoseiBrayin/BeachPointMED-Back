from fastapi import HTTPBearer, Request

class JWTBearer(HTTPBearer):
    async def __call__(self, request:Request):
        return await super().__call__(request)