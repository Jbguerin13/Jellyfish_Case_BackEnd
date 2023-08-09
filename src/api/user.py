import uvicorn
import sys
import asyncio, schedule
from datetime import datetime
from fastapi import FastAPI, Body, Depends, HTTPException
# from auth.jwt_handler import signJWT
# from auth.jwt_bearer import jwtBearer
from sqlmodel import Field, SQLModel, Session, select
from typing import Optional
from .entrypoint import app  #peut-être un pb d'import circulaire ici
from ..database import engine

"""User model management"""

# Class defining the table "User" that the user will complete


class User(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str


# 1.user signup [create a new user]


@app.post("/user/signup", tags=["User"])
async def user_signup(user: User):
    with Session(engine) as session :
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    # return signJWT(user.email)

# @app.post("/user/signup", tags=["User"])
# async def user_signup(user: User, db: db_dependency):
#     db_users = models.User(email=user.email, password=user.password)
#     db.add(db_users)
#     db.commit()
#     db.refresh(db_users)
#     return {"message": "User registered successfully"}
# Function to verify if user is existing


# def check_user(data: UserLoginSchema, db: db_dependency):
#     user = db.query(models.User).filter(models.User.email == data.email, models.User.password == data.password).first()
#     return user is not None


# # 2.user login
# @app.post("/user/login", tags=["User"])
# def user_login(user: UserLoginSchema):
#     if check_user(user):
#         return signJWT(user.email)
#     else:
#         raise HTTPException(status_code=404, detail="User not found")


# # 3. Update User


# @app.post("/user/update", tags=["User"])
# async def update_user(request: UserLoginSchema, db: db_dependency):
#     db_user = crud.update_user(
#         db,
#         user_id=request.parameter.id,
#         email=request.parameter.email,
#         password=request.parameter.password,
#     )


# # 4. Remove User


# @app.delete("/user/Remove", tags=["User"], dependencies=[Depends(jwtBearer())])
# async def delete_user(id: int, db: db_dependency):
#     crud.remove_user(db, user_id=id)
#     return {"message": "data deleted succefully"}
