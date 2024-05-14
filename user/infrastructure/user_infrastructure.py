from db.connection import Session
from models import response
from user.model import user_model, user_response
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def create_user(user_data: user_response.UserResponse):
    try:
        user = user_model.User(**user_data.dict())
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
    user = session.query(user_model.User).filter(
        (user_model.User.email == user.email) & (user_model.User.password == user.password)).first()
    session.close()
    if user is None:
        raise HTTPException(status_code=404,
                            detail=response.APIResponse(status="error", message="User not found", status_code=404).__dict__)
    user_dict = {key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}
    return response.APIResponse(data=user_dict, status="success", message="User has been successfully logged in")

def get_user():
    try:
        session = Session()
        users = session.query(user_model.User).all()
        session.close()
        users_list = [{key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'} for user in users]
        return response.APIResponse(data=users_list, status="success", message="Users have been successfully retrieved")
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=response.APIResponse(status="error", message=str(e), status_code=500).__dict__)
    
def get_user_by_cedula(cedula):
    try:
        session = Session()
        user = session.query(user_model.User).filter(user_model.User.cedula == cedula).first()
        session.close()
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=response.APIResponse(status="error", message=str(e), status_code=500).__dict__)
    if user is None:
        raise HTTPException(status_code=404,
                            detail=response.APIResponse(status="error", message="User not found", status_code=404).__dict__)
    user_dict = {key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}
    return response.APIResponse(data=user_dict, status="success", message="User has been successfully retrieved",status_code=200)