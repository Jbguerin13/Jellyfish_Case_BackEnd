import uvicorn
import sys
import asyncio, schedule
import requests, time, sched
from datetime import datetime
from decouple import config
from fastapi import FastAPI, Body, Depends, HTTPException
from models import AlertSchema, ShedSchema, PostSchema, UserSchema, UserLoginSchema
from aux_function import run_alert, schedule_task, background_scheduler
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer



# create a db for testing
posts = [
    {"id" : 1,
     "title" : "penguins",
     "content" : "group of aquatic flightless birds"
     },
    {"id" : 2,
     "title" : "tigers",
     "content" : "very big cat"
     },
    {"id" : 3,
     "title" : "koalas",
     "content" : "marsupial nativ to Australia"
     }
]

users = []

alerts = []

coinBTC = []

scheduler = sched.scheduler(time.time, time.sleep)

KEY = config("key")

app = FastAPI()


# 1.Get alert
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


# 2.Get single alert by id
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return HTTPException(
            status_code=404, detail="Post with this ID does not exist"
        )
    for post in posts:
        if post["id"] == id:
            return {"data": post}


# 3.Post a blog post [A handler for creating a post]
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_posts(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return HTTPException(status_code=200, detail="Info added")


# 4.user signup [create a new user]
@app.post("/user/signup", tags=["User"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

#Function to verify if user is existing
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# 5.user login
@app.post("/user/login", tags=["User"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        raise HTTPException(status_code=404, detail="User not found")

# 6.get current BTC value in USD
@app.get("/coin", dependencies= [Depends(jwtBearer())],tags= ["coin"])
def get_coinBTC():

    url = f"https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {"X-CoinAPI-Key": KEY}
    response = requests.get(url, headers=headers).json()
    result = round(response["rate"], 2)

    return {
        "date" : datetime.now().date().strftime('%d/%m/%Y'),
        "Current value of BTC in USD" : result
    }

# 6.Create an alert

@app.post("/alert",dependencies= [Depends(jwtBearer())], tags= ["alerts"])
def add_alert(alert: AlertSchema = Body(default= None)):

    if alert.upper_or_lower == "lower" or alert.upper_or_lower == "upper" :
        alerts.append(alert)
    else:
        raise HTTPException(status_code= 404, detail= "incorrect input")


# 6.Manage notif

@app.post("/start-notif", dependencies= [Depends(jwtBearer())], tags= ["notif"])
async def start_notif(background_scheduler):

    asyncio.create_task(background_scheduler())
    return {"message": "Notif started"}

@app.post("/stop-notif", dependencies= [Depends(jwtBearer())], tags= ["notif"])
async def stop_notif():
    schedule.clear()
    return {"message": "Notif stopped"}
