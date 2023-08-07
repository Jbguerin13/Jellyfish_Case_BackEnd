from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

DATABASE_URL = config("db_url")

#create a DB engine managing connection to DB and executing SQL queries
engine = create_engine(DATABASE_URL)

#create a session class --> interface for interacting with DB and performing operation like crud
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

#create a base class to define DB tables
Base = declarative_base()
