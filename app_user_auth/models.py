from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import BOOLEAN, Column, ForeignKey, Integer, String
from database import engine, SessionLocal
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass
from typing import List, Annotated, Optional
from fastapi import Depends
from uuid import uuid4

"""Alert model management"""
#Class defining the table "alerts" in the DB
class Base(DeclarativeBase, MappedAsDataclass):
    pass

class Mixin:
    create_alert : Mapped[int] = mapped_column()
    update_alert : Mapped[Optional[int]] = mapped_column(default= None, init= False)

class Alert(Base, Mixin):
    __tablename__ = "alerts"

    alert_id : Mapped[int] = mapped_column(primary_key = True, index= True)
    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    value_alert : Mapped[int] = mapped_column()
    setup_time_min : Mapped[int] = mapped_column()
    upper_or_lower : Mapped[str] = mapped_column()


#Class defining the model "Alert" that the user will complete to crud an alert

class AlertSchema(BaseModel) :

    upper_or_lower : str = Field(default = None)
    value_alert : int = Field(defaut = None)
    setup_time_min : int = Field(default = None)

    class Config :

        schema_exemple = {
            "alert_demo" : {
                "upper_or_lower" : "lower",
                "value_alert" : 20000,
                "setup_time_min" : 10
            }
        }

"""User model management"""

#Class defining the table "User" that the user will complete

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key = True, index= True)
    email : Column(EmailStr, index= True)
    password : Column(String, index= True)


#Class defining the model "User" that the user will complete to crud a new user

class UserSchema(BaseModel):

    email : EmailStr = Field(default= None)
    password : str = Field(default= None)

    class Config:
        the_schema = {
            "user_demo" :{
                "email" : "tigrus@gmail.com",
                "password" : "123abc"
            }
        }

#Class defining the model "UserLogin" that the user will complete to LogIn a session

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default= None)
    password : str = Field(default= None)
    class Config:
        the_schema = {
            "user_demo" :{
                "email" : "tigrus@gmail.com",
                "password" : "123abc"
            }
        }

#Function allow to endpoints that need to interact with the database even if there is an exception

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ensures that the db session is properly managed and closed after the endpoint has finished processing

db_dependency = Annotated[Session, Depends(get_db)]
