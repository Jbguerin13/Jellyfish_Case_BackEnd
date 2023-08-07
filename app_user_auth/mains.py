import uvicorn
import sys, models, crud
import asyncio, schedule
import requests, time, sched
from datetime import datetime
from decouple import config
from fastapi import FastAPI, Body, Depends, HTTPException
from models import AlertSchema, ShedSchema, UserSchema, UserLoginSchema, get_db, db_dependency
from aux_function import run_alert, schedule_task, background_scheduler
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer




scheduler = sched.scheduler(time.time, time.sleep)

KEY = config("key")

app = FastAPI()


# 1.user signup [create a new user]

@app.post("/user/signup", tags=["User"])
async def user_signup(user: UserSchema, db: db_dependency):
    db_users = models.User(email = user.email, password = user.password)
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return {"message" : "User registered successfully"}
    #return signJWT(user.email)


#Function to verify if user is existing

def check_user(data: UserLoginSchema, db: db_dependency):
    user = db.query(models.User).filter(
        models.User.email == data.email,
        models.User.password == data.password
        ).first()
    return user is not None

# 2.user login
@app.post("/user/login", tags=["User"])
def user_login(user: UserLoginSchema):
    if check_user(user):
        return signJWT(user.email)
    else:
        raise HTTPException(status_code=404, detail="User not found")


# 3. Update User

@app.post("/user/update", tags= ["User"])
async def update_user(request: UserLoginSchema, db: db_dependency):
    db_user = crud.update_user(
        db,
        user_id= request.parameter.id,
        email= request.parameter.email,
        password= request.parameter.password,
    )


# 4. Remove User

@app.delete("/user/Remove", tags= ["User"], dependencies= [Depends(jwtBearer())])
async def delete_user(id: int, db: db_dependency):
    crud.remove_user(
        db,
        user_id = id
    )
    return {"message" : "data deleted succefully"}


# 5.Create an alert

@app.post("/alert",dependencies= [Depends(jwtBearer())], tags= ["alerts"])
async def add_alert(alert: AlertSchema, db= db_dependency):

    db_alert = models.Alert(
        upper_lower = alert.upper_or_lower,
        value_alert = alert.value_alert,
        setup_time_min = alert.setup_time_min)

    if not alert.upper_or_lower == "lower" or alert.upper_or_lower == "upper" :

        raise HTTPException(status_code= 404, detail= "incorrect input")

    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return {"message" : "Alert Created successfully"}


# 6.Update an alert
@app.post("/alert/update",dependencies= [Depends(jwtBearer())], tags= ["alerts"])
async def update_alert(request: AlertSchema, db: db_dependency):

    db_alert = crud.update_alert(
        db,
        alert_id= request.parameter.alert_id,
        upper_or_lower= request.parameter.upper_or_lower,
        value_alert= request.parameter.value_alert,
        setup_time_min= request.parameter.setup_time_min
    )


# 6.Remove an alert
@app.delete("/alert/remove", dependencies= [Depends(jwtBearer())], tags= ["Alert"])
async def remove_alert(id: int, db:db_dependency):
    crud.remove_alert(db, alert_id= id)

    return {"message" : "alert deleted successfully"}


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

# 6.Manage notif

@app.post("/start-notif", dependencies= [Depends(jwtBearer())], tags= ["notif"])
async def start_notif(background_scheduler):

    asyncio.create_task(background_scheduler())
    return {"message": "Notif started"}

@app.post("/stop-notif", dependencies= [Depends(jwtBearer())], tags= ["notif"])
async def stop_notif():
    schedule.clear()
    return {"message": "Notif stopped"}
