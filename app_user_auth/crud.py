from sqlalchemy.orm import Session
from pydantic import EmailStr
from models import User, UserSchema, db_dependency, Alert



#Get all data from user table

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# Get by id user and alert data


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_alert_by_id(db: Session, alert_id: int):
    return db.query(Alert).filter(Alert.id == alert_id).first()



# function to Update user and alert data

def update_user(db: Session, user_id: int, email: EmailStr, password: str):
    db_user = get_user_by_id(db = db, user_id = user_id)
    db_user.email = email
    db_user.password = password
    db.commit()
    db.refresh()
    return db_user

def update_alert(db: Session,
                 alert_id: int,
                 upper_or_lower: str,
                 value_alert: int,
                 setup_time_min: int):

    db_alert = get_alert_by_id(db = db, alert_id = alert_id)
    db_alert.upper_or_lower = upper_or_lower
    db_alert.value_alert = value_alert
    db_alert.setup_time_min = setup_time_min
    db.commit()
    db.refresh()
    return db_alert


# function to delete user and alert data by id

def remove_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db.delete(db_user)
    db.commit()

def remove_alert(db: Session, alert_id: int):
    db_alert = get_user_by_id(db=db, alert_id= alert_id)
    db.delete(db_alert)
    db.commit()
