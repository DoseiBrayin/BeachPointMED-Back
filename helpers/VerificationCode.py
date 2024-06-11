from datetime import datetime, timedelta
import os
import jwt
from dotenv import load_dotenv

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
        if payload['exp'] < datetime.utcnow():
            return 'Token expirado. Por favor solicite uno nuevo.'
    except jwt.ExpiredSignatureError:
        return 'Token expirado. Por favor solicite uno nuevo.'
    except jwt.InvalidTokenError:
        return 'Token inválido. Por favor solicite uno nuevo.'