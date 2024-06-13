from db.connection import Session
from models import response
from user.model import user_response
from db.models.BPDataBase import Users, Rol
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from JWT.jwtmanager import create_token


def create_user(user_data: user_response.UserResponse):
    try:
        user = Users(**user_data.dict())
        session = Session()
        session.add(user)
        session.commit()
        session.close()
        user_dict = {key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}
        return response.APIResponse(data=user_dict, status="success", message="User has been created successfully")
    except IntegrityError as e:
        if 'duplicate key value violates unique constraint' in str(e):
            raise HTTPException(status_code=400,
                                detail=response.APIResponse(status="error", message="Duplicate key value violates unique constraint", status_code=400).__dict__)
        else:
            raise HTTPException(status_code=400,
                                detail=response.APIResponse(status="error", message=str(e), status_code=400).__dict__)
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=response.APIResponse(status="error", message=str(e), status_code=500).__dict__)

def login(user: user_response.LoginResponse):
    session = Session()
    user = session.query(Users).filter(
        (Users.email == user.email) & (Users.password == user.password)).first()
    session.close()
    if user is None:
        raise HTTPException(status_code=404,
                            detail=response.APIResponse(status="error", message="User not found", status_code=404).__dict__)
    user_dict = {key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}
    return response.APIResponse(data=create_token(user_dict), status="success", message="User has been successfully logged in")

def get_user():
    try:
        session = Session()
        users = session.query(
            Users.cedula,
            Users.phone_number,
            Users.email,
            Users.name,
            Users.password,
            Users.is_employee,
            Rol.type_rol
        ).join(
            Rol, Users.fk_rol == Rol.id
        ).order_by(
            Users.id
        ).all()
        session.close()
        users_list = [dict(row._asdict()) for row in users]


        if not users_list:
            return response.APIResponse(
                data=None, 
                status="success", 
                message="There are no users", 
                status_code=200
            )
        
        return response.APIResponse(
            data=users_list, 
            status="success", 
            message="Users have been successfully retrieved", 
            status_code=200
        )
    
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=response.APIResponse(status="error", message=str(e), status_code=500).__dict__)