from pydantic import BaseModel

#Data Model

# class User(Model):
#     id = fields.IntField(pk= True)
#     fullname =  fields.CharField(100, unique= True)  #Change fullname --> username
#     password = fields.CharField(200)
#     alerts : fields.ReverseRelation["Alert"]

# class Alert(Model):
#     user : fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
#         "models.User", related_name= "alerts")
#     id = fields.IntField(pk= True)
#     alert_above_or_under_value = fields.CharField(50, unique= True)
#     value_dollar = fields.IntField(pk= True)
