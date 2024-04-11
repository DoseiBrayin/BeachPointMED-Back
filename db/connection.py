from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from dotenv import load_dotenv


load_dotenv()

# Connection string with credentials (replace with your actual password)
connection_string = environ.get('DATABASE_URL')

# Create the engine object
engine = create_engine(connection_string)

# Create a session object
Session = sessionmaker(bind=engine)

# Create a base class
Base = declarative_base()

try:
  # Print confirmation message
  print("Connection established successfully using SQLAlchemy!")

except Exception as e:
  print("Error connecting to PostgreSQL database:", e)


# Engine objects manage connections, so no need to explicitly close them
# However, you can test a connection using the following
# print(engine.connect())
