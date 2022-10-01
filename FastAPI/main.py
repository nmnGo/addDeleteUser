import code
from http.client import HTTPException
from this import d
from fastapi import FastAPI;HTTPException
from models import User,Gender,Role
from typing import List
from uuid import uuid4,UUID

app= FastAPI()

db: List[User] = [
    
    User(
        id=UUID("451db6a5-b6c8-4a21-82ca-d8f5dd7fb5fd"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.female,
        roles=[Role.student]
    ),
    
    User(
        id=uuid4(),
        first_name="Naman",
        last_name="Hissab",
        gender=Gender.male,
        roles=[Role.student, Role.admin]
    )
]
    

@app.get("/")
async def root():
    return {"Hello":"Worlds", " oasnca":"cdwoc"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id" : user.id}

@app.delete("/api/v1/usera/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return 
        raise HTTPException(
            status_code=404,
            detail=f"user id does not exist"
        )
