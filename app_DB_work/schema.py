from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel

T = TypeVar("T")


# Define UserSchema BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True


# Define UserLoginSchema BaseModel


class UserLoginSchema(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# Define Response for the user


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
