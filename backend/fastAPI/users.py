from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

# Create
users_db = [User(id=1, name="Jialiang", surname="Ye", age=27, url="www.google.es"),
            User(id=2, name="Jordi", surname="Yan", age=17, url="google"),
            User(id=3, name="George", surname="Ye Yan", age=37, url="www.google.es")]


@app.get("/users")
async def list_users():
    return users_db


@app.get("/list-users")
async def users():
    return [{"name": "Jialiang", "surname": "Ye", "age": 27, "url": "www.google.es"},
            {"name": "Jordi", "surname": "Yan", "age": 17, "url": "google"},
            {"name": "George", "surname": "Ye Yan", "age": 37, "url": "www.google.es"}]


# Path
@app.get("/user/{id}")
async def users(id: int):
    for user in users_db:
        if user.id == id:
            return user
        

@app.get("/user-lambda/{id}")
async def users(id: int):
    users = filter(lambda user: user.id == id, users_db)

    try:
        return list(users)[0]
    except:
        return [{"error": "No existe dicho usuario"}]
    

# Query
@app.get("/user-query")
async def users(id: int):
    users = filter(lambda user: user.id == id, users_db)

    try:
        return list(users)[0]
    except:
        return [{"error": "No existe dicho usuario"}]


# Create
@app.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_db.append(user)
        return user


# Update
@app.put("/user/")
async def user(user: User):
    found = False
    for index, userlist in enumerate(users_db):
        if userlist.id == user.id:
            users_db[index] = user
            found = True
    
    if not found:
        return "No existe el usuario a modificar"
    else:
        return user


# Delete
@app.delete("/user/")
async def user(id: int):
    for index, userlist in enumerate(users_db):
        if userlist.id == id:
            del users_db[index]
            return "Usuario eliminado"
    return "Usuario no encontrado"


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_db)

    try:
        return list(users)[0]
    except:
        return [{"error": "No existe dicho usuario"}]















