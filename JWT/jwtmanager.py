from jwt import encode, decode
from os import environ
from dotenv import load_dotenv

def create_token(data:dict ):
    return str(encode(payload=data, key=load_dotenv().get('SECRET_KEY'), algorithm='HS256'))

def validate_token(token:str):
    try:
        return decode(token, load_dotenv().get('SECRET_KEY'), algorithms='HS256')
    except:
        return False