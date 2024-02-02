
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

api = FastAPI()


## Models
class User(BaseModel):
    id: int
    name: str
    surname: str
    city: str
    age: int

users_list = [
    User(id = 1, name = "jhon", surname = "doe", city = "Utah", age = 33),
    User(id = 2, name = "michael", surname = "jackson", city = "California", age = 35),
    User(id = 3, name = "frank sinatra", surname = "doe", city = "New Jersey", age = 50),
              ]

## API
@api.get("/users")
async def get_users():
    return users_list

@api.get("/users/{id}")
async def get_users_by_id(id: int):
    return search_users(id)
    
@api.get("/users/query/")
async def get_users_params_by_id(id: Union[int, None] = None):
    return search_users(id)
    

@api.post("/users")
async def post_users():
    return "lsita usuarios"

@api.put("/users")
async def update_users():
    return "lsita usuarios"

@api.delete("/users")
async def delete_users():
    return "lsita usuarios"


def search_users(id):
    #return list(filter(lambda  user : user.id == id , users_list))[0] if id <= len(users_list) else f"Usuario no encontrado"
    try:
        return list(filter(lambda  user : user.id == id , users_list))[0]
    except:
        return {"error": "Usuario no encontrado"}