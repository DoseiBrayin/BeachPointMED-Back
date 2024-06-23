# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from locations.router import locationsRouter
from timeCourts.router import timeCourts_router
from user.router import user_router
from products.router import products_router
from payment.router import paymente_router
from helpers.scheduler import scheduler

app = FastAPI()

# Inicia el planificador
scheduler.start()

# Agrega las rutas de la API
app.include_router(locationsRouter.router, prefix="/locations")
app.include_router(timeCourts_router.router, prefix="/timeCourts")
app.include_router(user_router.router, prefix="/user")
app.include_router(products_router.router, prefix="/products")
app.include_router(paymente_router.router, prefix="/payment")

# Lista de orígenes permitidos
origins = [
    "https://beachpointmed.pages.dev",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

# Agrega el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



