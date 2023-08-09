from sqlalchemy.orm import Session
from pydantic import EmailStr


def update_alert(db: Session, alert_id: int, upper_or_lower: str, value_alert: int, setup_time_min: int):

    db_alert = get_alert_by_id(db=db, alert_id=alert_id)
    db_alert.upper_or_lower = upper_or_lower
    db_alert.value_alert = value_alert
    db_alert.setup_time_min = setup_time_min
    db.commit()
    db.refresh()
    return db_alert


def remove_alert(db: Session, alert_id: int):
    db_alert = get_user_by_id(db=db, alert_id=alert_id)
    db.delete(db_alert)
    db.commit()


def get_alert_by_id(db: Session, alert_id: int):
    return db.query(Alert).filter(Alert.id == alert_id).first()
