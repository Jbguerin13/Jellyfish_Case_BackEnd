from sqlalchemy import Column, Integer, String
from config import Base

#Define table user

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username =  Column(String)
    email = Column(String)
    password = Column(String)
   # alerts : fields.ReverseRelation["Alert"]
