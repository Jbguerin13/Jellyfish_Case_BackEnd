from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):

    id : int = Field(default= None)
    title : str = Field(default= None)
    content : str = Field(default= None)

    class Config:

        schema_extra = {
            "post_demo" :{
                "title" : "some title exemple",
                "content" : "some content example"
            }
        }

class ShedSchema(BaseModel):

    time_alert_sec : int = Field (default= 600)

    class Config:

        schema_exp = {
            "shed_demo" : {
                "time_alert_sec" : 600
            }
        }

class AlertSchema(BaseModel) :

    upper_or_lower : str = Field(default= None)
    value_alert : int = Field(defaut = None)

    class Config :

        schema_exemple = {
            "alert_demo" : {
                "upper_or_lower" : "lower",
                "value_alert" : 20000
            }
        }

class UserSchema(BaseModel):

    fullname : str = Field(default= None)
    email : EmailStr = Field(default= None)
    password : str = Field(default= None)
    class Config:
        the_schema = {
            "user_demo" :{
                "name" : "tigrus",
                "email" : "tigrus@gmail.com",
                "password" : "123abc"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default= None)
    password : str = Field(default= None)
    class Config:
        the_schema = {
            "user_demo" :{
                "email" : "tigrus@gmail.com",
                "password" : "123abc"
            }
        }
