from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, user_list_schema
from bson import ObjectId

router = APIRouter(prefix="/userdb", 
                   tags=["UserDB"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

users_db = []

# Read
@router.get("/", response_model=list[User])
async def list_users():
    return user_list_schema(db_client.users.find())

@router.get("/{id}")
async def users(id: str):
    return search_user("_id", ObjectId(id))


# Create
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user_by_email(user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya existe")

    user_json = dict(user) # Pasa el user a formato json
    del user_json["id"] # Elimina el campo id para que el id se autogenere

    # {local.}user es el nombre de la base de datos sobre la que opera, 
    # si se indica en client.py el .local no hace falta añadirlo en el resto de peticiones
    id = db_client.users.insert_one(user_json).inserted_id
    
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)


# Update
@router.put("/", response_model=User)
async def user(user: User):
    try:
        user_json = dict(user)
        db_client.users.find_one_and_replace({"_id":ObjectId(user.id)}, user_json)
    except:
        return "No existe el usuario a modificar"     
    else:
        return user


# Delete
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}



def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        user_json = user_schema(user)
        return User(**user_json)
    except:
        return [{"error": "No existe dicho usuario"}]

def search_user_by_email(email: str):
    try:
        user = db_client.users.find_one({"email": email})
        user_json = user_schema(user)
        return User(**user_json)
    except:
        return [{"error": "No existe dicho usuario"}]
