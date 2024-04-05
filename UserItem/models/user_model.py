# models.py
from pydantic import BaseModel
#Aqui creamos el modelo de datos que se va a utilizar en la aplicacion
class Item(BaseModel):
    name: str
    description: str
    price: float