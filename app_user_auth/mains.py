import uvicorn
import sys
from fastapi import FastAPI, Body, Depends, HTTPException
from app_user_auth.schemas import AlertSchema, UserSchema, UserLoginSchema
from app_user_auth.auth.jwt_handler import signJWT
from app_user_auth.auth.jwt_bearer import jwtBearer


# create a db for testing
alerts = [
    {"id": 1, "up_or_down": "down", "value $": 2000},
    {"id": 2, "up_or_down": "up", "value $": 10000},
    {"id": 3, "up_or_down": "down", "value $": 5000},
]

users = []


app = FastAPI()


# 0.Get - for testing
@app.get("/", tags=["home"])
def hello():
    return {"hello": "world"}


# 1.Get alert
@app.get("/alerts", tags=["alerts"])
def get_alerts():
    return {"data": alerts}


# 2.Get single alert by id
@app.get("/alerts/{id}", tags=["alerts"])
def get_one_post(id: int):
    if id > len(alerts):
        return HTTPException(
            status_code=404, detail="Alert with this ID does not exist"
        )
    for alert in alerts:
        if alert["id"] == id:
            return {"data": alert}


# 3.Post a blog alert [A handler for creating an alert]
@app.post("/alerts", dependencies=[Depends(jwtBearer())], tags=["alerts"])
def add_alerts(alert: AlertSchema):
    alert.id = len(alerts) + 1
    alerts.append(alert.dict())
    return HTTPException(status_code=200, detail="Info added")


# 4.user signup [create a new user]
@app.post("/user/signup", tags=["User"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        raise HTTPException(status_code=403, detail="User not found")


# Recording FastAPI app with Tortoise-ORM
