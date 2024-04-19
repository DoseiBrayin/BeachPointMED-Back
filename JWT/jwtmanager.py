from jwt import encode, decode
import os
from dotenv import load_dotenv

load_dotenv()

def create_token(data:dict ):
    return str(encode(payload=data, key=os.getenv('SECRET_KEY'), algorithm='HS256'))

def validate_token(token:str):
    try:
        return decode(token, key=os.getenv('SECRET_KEY'), algorithms='HS256')
    except Exception as e:
        return e.__str__()