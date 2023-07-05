from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import UserSchema, UserLoginSchema, Response
import crud


router = APIRouter()

#Get all database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Create a new user

@router.post('/create')
async def create(request: UserLoginSchema, db: Session=Depends(get_db())):
    crud.create_user(db, request.parameter)
    return Response(code = 200, status= "Ok", message= "Book created successfully").dict(exclude_none = True)


#Get user data

@router.get("/")
async def get (db:Session=Depends(get_db())):
    _user = crud.get_user(db, 0, 100)
    return Response(code= 200, status= "OK", message= "Success fetch all data", result= _user).dict()


#Get user data by user_id

@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, id)
    return Response(code= 200, status= "Ok", message= "Success get data", result= _user).dict(exclude_none= True)


#Update user data

@router.post("/update")
async def update_book (request: UserLoginSchema, db: Session = Depends(get_db)):
    _user = crud.update_user(db, user_id= request.parameter.id,
                             email= request.parameter.email,
                             password=request.parameter.password)


#Delete user by user_id

@router.delete("/{id}")
async def delete(id:int, db:Session = Depends(get_db())):
    crud.remove_user(db, user_id= id)
    return Response(code= 200, status= "OK", message= "Success delete data").dict(exclude_none= True)
