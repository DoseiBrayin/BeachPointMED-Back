import uvicorn
from db import connection

if __name__ == "__main__":
    connection.engine.connect()
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)