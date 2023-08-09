from sqlalchemy.orm import Session
from pydantic import EmailStr
from models import User, UserSchema, db_dependency, Alert

# Get all data from user table


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# Get by id user and alert data


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def remove_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db.delete(db_user)
    db.commit()


# function to Update user and alert data


def update_user(db: Session, user_id: int, email: EmailStr, password: str):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.email = email
    db_user.password = password
    db.commit()
    db.refresh()
    return db_user
