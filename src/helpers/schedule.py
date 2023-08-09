import schedule, time, asyncio
from models import AlertSchema
from alert import run_alert
from fastapi import FastAPI, Body, Depends, HTTPException


def schedule_task(alert: AlertSchema):

    schedule.every(alert.setup_time_min).do(run_alert)

    while True:
        schedule.run_pending()
        time.sleep(1)


async def background_scheduler():

    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, schedule_task)
