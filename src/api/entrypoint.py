from fastapi import FastAPI
from sqlmodel import SQLModel


app = FastAPI()

from . import user
from ..database import engine

SQLModel.metadata.create_all(engine)



#Si jamais pb import circu, mettre les from . import fichiers après app
