import schedule, time, asyncio
from mains import get_coinBTC
from models import AlertSchema
from fastapi import FastAPI, Body, Depends, HTTPException



def run_alert(alert : AlertSchema = Body()):

    response = {"message" : "alert activate"}

    if alert.upper_or_lower == "lower" :

        if alert.value_alert > get_coinBTC()["Current value of BTC in USD"] :
            response = {"message" : f"Carefull, the value of BTC in USD is lower than {alert.value_alert} from now"}

    if alert.upper_or_lower == "upper" :

        if alert.value_alert < get_coinBTC()["Current value of BTC in USD"] :
            response = {"message" : f"Carefull, the value of BTC in USD is upper than {alert.value_alert} from now"}

    print(response)


def schedule_task(alert : AlertSchema):

    schedule.every(alert.setup_time_min).do(run_alert)

    while True:
        schedule.run_pending()
        time.sleep(1)


async def background_scheduler():

    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, schedule_task)
