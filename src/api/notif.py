import uvicorn
import sys
import asyncio, schedule
import requests, time, sched
from datetime import datetime
from decouple import config
from fastapi import FastAPI, Body, Depends, HTTPException
from helpers.schedule import background_scheduler
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer
from .entrypoint import app

@app.post("/start-notif", dependencies=[Depends(jwtBearer())], tags=["notif"])
async def start_notif():

    asyncio.create_task(background_scheduler())
    return {"message": "Notif started"}


@app.post("/stop-notif", dependencies=[Depends(jwtBearer())], tags=["notif"])
async def stop_notif():
    schedule.clear()
    return {"message": "Notif stopped"}
