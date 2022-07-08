""" SQL Alchemy is a DB wrapper
1- We need to create an engine
2- We need to create a session
"""
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Se realiza la función que va a crear el motor con SQL Alchemy
def get_engine(user, passwd, host, port, db):
    url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine
