import pandas as pds
from sqlalchemy import create_engine, text
import psycopg2
# Pandas Login Information
pandas_username = "postgres"
pandas_pass = "Your Postgres Password"

# Pandas Server Connection
alchemyEngine = create_engine(f"postgresql+psycopg2://{pandas_username}:{pandas_pass}@localhost/dvdrental",
                              pool_recycle=3600)

# Try to Connect PostgreSQL Server
dbConnection = None
try:
    dbConnection = alchemyEngine.connect()
    print("Connection Successful")
except psycopg2.OperationalError as e:
    print(f"Connection Failed !!\nError: {e}\nCheck if the PostgreSQL Server is OK")

# Write the SQL Query

pos_sql_query = """SELECT title,film_id FROM film WHERE film_id < 1000 AND title LIKE 'B%' ; """

# Read Data From PostgreSQL

dataFrame = pds.read_sql(text(pos_sql_query), dbConnection)
print(dataFrame)
