from sqlalchemy import create_engine

# Connection string with credentials (replace with your actual password)
connection_string = 'postgresql://db_beachpoint_user:SfCD2RimtvfNPZ43XHeapgtImPlmdXUz@dpg-coa2ln0cmk4c73e8ridg-a.oregon-postgres.render.com/db_beachpoint'

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
