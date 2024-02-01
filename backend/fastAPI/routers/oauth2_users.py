from fastapi import Depends, APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    name: str
    email: str
    disabled: int

class UserDB(User):
    password: str


user_db = {
    "lele": {
        "username": "lele",
        "name": "Jordi",
        "email": "jordilele@mail.com",
        "disabled": False,
        "password": "123456"
    },
    "aitor": {
        "username": "tortilla",
        "name": "Aitor",
        "email": "aitortilla@mail.com",
        "disabled": True,
        "password": "1234"
    },
    "camela": {
        "username": "camela",
        "name": "Benito",
        "email": "benitocamela@mail.com",
        "disabled": True,
        "password": "1234"
    },
    "kck": {
        "username": "kck",
        "name": "ick",
        "email": "ickkck@mail.com",
        "disabled": True,
        "password": "1234"
    }
}


def search_user(username: str):
    if username in user_db:
        return User(**user_db[username])
    
def search_user_db(username: str):
    if username in user_db:
        return UserDB(**user_db[username])
    

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token) # En este caso porque el token que devuelve es el username
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Credenciales incorrectas",
                            headers={"WWW-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario deshabilitado")
    
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = user_db.get(form.username)
    
    if not user:
        raise HTTPException(status_code=400, detail="El usuario no existe")

    user = search_user_db(form.username)

    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
