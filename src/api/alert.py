import uvicorn
import sys
import asyncio, schedule
from datetime import datetime
from fastapi import Body, Depends, HTTPException
# from auth.jwt_handler import signJWT
# from auth.jwt_bearer import jwtBearer
from sqlmodel import Field, SQLModel, Session, select
from typing import Optional
from .entrypoint import app  #peut-être un pb d'import circulaire ici
from ..database import engine


from database import engine, SessionLocal
from sqlmodel import Field, Session, SQLModel, create_engine
from .entrypoint import app


"""Alert model management"""


class Alert(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value_alert: Optional[int] = Field()
    setup_time_min: Optional[int] = Field()
    upper_or_lower: str = Field()
    user_id: Optional[int] = Field(default= None, foreign_key=("user.id"))


# 1.Create an alert

@app.post("/alert", dependencies=[Depends(jwtBearer())], tags=["alerts"])
async def add_alert(alert: AlertSchema, db=db_dependency):

    db_alert = models.Alert(
        upper_lower=alert.upper_or_lower, value_alert=alert.value_alert, setup_time_min=alert.setup_time_min
    )

    if not alert.upper_or_lower == "lower" or alert.upper_or_lower == "upper":

        raise HTTPException(status_code=404, detail="incorrect input")

    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return {"message": "Alert Created successfully"}


# 6.Update an alert
# @app.post("/alert/update", dependencies=[Depends(jwtBearer())], tags=["alerts"])
# async def update_alert(request: AlertSchema, db: db_dependency):

#     db_alert = crud.update_alert(
#         db,
#         alert_id=request.parameter.alert_id,
#         upper_or_lower=request.parameter.upper_or_lower,
#         value_alert=request.parameter.value_alert,
#         setup_time_min=request.parameter.setup_time_min,
#    )


# 6.Remove an alert
# @app.delete("/alert/remove", dependencies=[Depends(jwtBearer())], tags=["Alert"])
# async def remove_alert(id: int, db: db_dependency):
#     crud.remove_alert(db, alert_id=id)

#     return {"message": "alert deleted successfully"}


# @app.get("/coin", dependencies=[Depends(jwtBearer())], tags=["coin"])
# def get_coinBTC():

#     url = f"https://rest.coinapi.io/v1/exchangerate/BTC/USD"
#     headers = {"X-CoinAPI-Key": KEY}
#     response = requests.get(url, headers=headers).json()
#     result = round(response["rate"], 2)

#     return {"date": datetime.now().date().strftime("%d/%m/%Y"), "Current value of BTC in USD": result}
