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