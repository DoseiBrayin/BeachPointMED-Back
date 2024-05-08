from pydantic import BaseModel

class UserResponse(BaseModel):
    id: str
    cedula: str
    phone_number: str
    email: str
    name: str
    password: str
    card_id: str
    is_employee: bool
    fk_rol: str