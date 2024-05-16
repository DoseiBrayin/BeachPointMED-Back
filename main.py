import uvicorn
from db import connection

if __name__ == "__main__":
    connection.engine.connect()
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)