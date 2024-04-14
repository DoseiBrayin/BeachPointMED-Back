# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from UserItem.router import userRouter
from locations.router import locationsRouter
from timeCourts.router import timeCourts_router
app = FastAPI()

# Agrega las rutas de la API
app.include_router(userRouter.router, prefix="/user")
app.include_router(locationsRouter.router, prefix="/locations")
app.include_router(timeCourts_router.router, prefix="/timeCourts")

# Lista de orígenes permitidos
origins = [
    "https://beachpointmed.pages.dev/",
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



