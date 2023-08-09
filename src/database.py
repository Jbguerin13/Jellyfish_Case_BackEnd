from sqlmodel import SQLModel, create_engine, Session, select
from typing import Optional, Annotated
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
#from decouple import config

DATABASE_URL = config("db_url")

# create a DB engine managing connection to DB and executing SQL queries
engine = create_engine(DATABASE_URL, echo= True)

# create a session class --> interface for interacting with DB and performing operation like crud
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class to define DB tables
#Base = declarative_base()

# Function allow to endpoints that need to interact with the database even if there is an exception


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# ensures that the db session is properly managed and closed after the endpoint has finished processing

# db_dependency = Annotated[Session, Depends(get_db)]
