from sqlalchemy import create_engine
from os import environ
from dotenv import load_dotenv

load_dotenv()

# Connection string with credentials (replace with your actual password)
connection_string = environ.get('DATABASE_URL')

print(environ.get('DATABASE_URL'))
# Create the engine object
engine = create_engine(connection_string)

try:
  # Print confirmation message
  print("Connection established successfully using SQLAlchemy!")

except Exception as e:
  print("Error connecting to PostgreSQL database:", e)


# Engine objects manage connections, so no need to explicitly close them
# However, you can test a connection using the following
# print(engine.connect())
