Para obtener información/documentación sobre el funcionamiento del endpoint, qué datos trae y qué información necesita, ve al endpoint `/docs`.

# Explicación de la arquitectura

El proyecto se compone principalmente de carpetas que llevan el nombre del caso de uso al que hacen referencia. Dentro de ellas, se utilizan dos carpetas distintas:

- **Models**: En esta carpeta se crean las clases con las que se manejará la base de datos.

- **Controllers**: Carpeta donde se crearán las funciones que procesan la información del endpoint (solicitudes a la base de datos, procesamiento de datos, etc).

La estructura de las carpetas del proyecto se organiza de la siguiente manera:

📁 Proyecto
-       📁 UserItem
- -         📁 controller
- - -           📄 user_controller.py
- -         📁 models
- - -           📄 user_model.py
-       📄 main.py


Además, está el archivo principal `main.py`, donde se encontrarán todos los endpoints que pueden ser consumidos por el frontend o el usuario.

En `main.py`, se configura CORS (Cross-Origin Resource Sharing) para permitir solicitudes desde ciertos orígenes. Esto se hace añadiendo un middleware CORS a la aplicación FastAPI:

```python
# Lista de orígenes permitidos
origins = [
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
)

