from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import BOOLEAN, column, ForeignKey, Integer, String
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated
from fastapi import Depends
from passlib.hash import bcrypt


#Class defining the table "alerts" in the DB

class Alert(Base):
    __tablename__ = "alerts"

    alert_id = column(Integer, primary_key = True, index= True)
    user_id = column(Integer, ForeignKey("users.id"))
    upper_or_lower = column(String, index= True)
    value_alert : column(Integer, index= True)
    setup_time_min : column(Integer, index= True)


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


#Class defining the table "User" that the user will complete

class User(Base):
    __tablename__ = "users"

    user_id = column(Integer, primary_key = True, index= True)
    email : column(EmailStr, index= True)
    password : column(String, index= True)


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
