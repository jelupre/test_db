from sqlalchemy import create_engine
from models import Base

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# get connection with postgres
connection = psycopg2.connect(user='postgres', password='1111')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# create DB
cursor = connection.cursor()
try:
    cursor.execute(f'create database test')
    print('DB is created')
except psycopg2.errors.DuplicateDatabase:
    print('This database has already existed')
finally:
    # сlose connection
    cursor.close()
    connection.close()

# connect to server PostgreSQL on localhost with psycopg2
engine = create_engine(f'postgresql+psycopg2://postgres:1111@localhost/test', echo=True)
engine.connect()

# create tables declared in 'models.py'
Base.metadata.create_all(engine)

# close connection
engine.dispose()
