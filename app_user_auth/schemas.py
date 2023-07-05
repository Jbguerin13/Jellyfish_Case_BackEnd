from pydantic import BaseModel, Field, EmailStr



class AlertSchema(BaseModel):
    id: int = Field(default= None)
    up_or_down: str = Field(default= None)
    value_dollar : int = Field(default= None)
    class Config :
        schema_alert = {
            "alert_demo" : {
                "alert above or under ?" : "under",
                "value in $" : 7000
            }
        }

class UserSchema(BaseModel):
    fullname : str = Field(default= None)
    email : EmailStr = Field(default= None)
    password : str = Field(default= None)

    class Config:
        schema_user = {
            "user_demo" : {
                "name" : "john",
                "email" : "john@example.com",
                "password" : "hello123"
            }
        }


class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default= None)
    password : str = Field(default= None)

    class Config:
        the_schema = {
            "user_demo" : {
                "email" : "help@exemple.com",
                "password" : "hello123"
            }
        }
