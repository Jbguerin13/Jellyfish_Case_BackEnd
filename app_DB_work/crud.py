from sqlalchemy.orm import Session
from model import User
from schema import UserSchema

# Get All user data


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# Get by id user data


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# Create user data


def create_user(db: Session, user: UserSchema):
    _user = User(username=user.username, email=user.email, password=user.password)
    db.add()
    db.commit()
    db.refresh(_user)
    return _user


# Remove user data


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


# Update user data


def update_user(db: Session, user_id: int, username: str, password: str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.username = username
    _user.password = password
    db.commit()
    db.refresh(_user)
    return _user
