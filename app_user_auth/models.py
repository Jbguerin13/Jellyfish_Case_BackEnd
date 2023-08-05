from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import BOOLEAN, column, ForeignKey, Integer, String
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated
from fastapi import Depends




class PostSchema(BaseModel):

    id : int = Field(default= None)
    title : str = Field(default= None)
    content : str = Field(default= None)

    class Config:

        schema_extra = {
            "post_demo" :{
                "title" : "some title exemple",
                "content" : "some content example"
            }
        }

class AlertSchema(Base):
    __tablename__ = "alerts"

    id = column(Integer, primary_key = True, index= True)
    user_id = column(Integer, ForeignKey("users.id"))
    upper_or_lower = column(String, index= True)
    value_alert : column(Integer, index= True)
    setup_time_min : column(Integer, index= True)

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

#Users table

class User(Base):
    __tablename__ = "users"

    id = column(Integer, primary_key = True, index= True)
    fullname = column(String, index= True)
    email : column(EmailStr, index= True)
    password : column(String, index= True)

class UserSchema(BaseModel):

    fullname : str = Field(default= None)
    email : EmailStr = Field(default= None)
    password : str = Field(default= None)
    class Config:
        the_schema = {
            "user_demo" :{
                "name" : "tigrus",
                "email" : "tigrus@gmail.com",
                "password" : "123abc"
            }
        }

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
