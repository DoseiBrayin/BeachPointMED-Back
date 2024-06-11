from datetime import datetime, timedelta
import os
import jwt
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

def generate_verification_token(email):
    secret_key = os.getenv('SECRET_KEY_CODE')
    if not secret_key:
        raise ValueError("Missing secret key")
    expiration = datetime.utcnow() + timedelta(minutes=5)  # El token expira en 10 minutos
    token = jwt.encode({'email': email, 'exp': expiration}, secret_key, algorithm='HS256')
    return token

def verify_verification_token(token):
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY_CODE'), algorithms='HS256')
        current_time = datetime.utcnow()
        current_timestamp = int(current_time.timestamp())
        if payload['exp'] > current_timestamp:
            return False
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token expirado. Por favor solicite uno nuevo.")
    except jwt.InvalidTokenError:
        return HTTPException(status_code=400, detail="Token inválido. Por favor solicite uno nuevo.")