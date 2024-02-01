from fastapi import Depends, APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

"""
Para JSON Web Token es necesario instalar el siguiente paquete:
    pip install "python-jose[cryptography]"
    pip install "passlib[bcrypt]"
"""
"""
El SECRET se ha obtenido por consola con el siguiente comando:
    openssl rand -hex 32
"""

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 # en minutos
SECRET = "4b478d8289dcf14b4d73bfd25fe52e419b58be62ab12659446bc9e662542a674"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    name: str
    email: str
    disabled: int

class UserDB(User):
    password: str


"""
Contraseñas obtenidas con un generador bcrypt (12 rounds): https://bcrypt-generator.com/
123456
1234
1234
1234
"""
user_db = {
    "lele": {
        "username": "lele",
        "name": "Jordi",
        "email": "jordilele@mail.com",
        "disabled": False,
        "password": "$2a$12$taMpP.AUAWtXNT/IpM6FcuZvOQqCJgvtKoy/UImYWPkQRYV6Ocady"
    },
    "aitor": {
        "username": "tortilla",
        "name": "Aitor",
        "email": "aitortilla@mail.com",
        "disabled": True,
        "password": "$2a$12$WSkiPnn4N7iuDSM7dIlmm.gIONFf1D14ARY.n87LjNy0f6ejgxPvK"
    },
    "camela": {
        "username": "camela",
        "name": "Benito",
        "email": "benitocamela@mail.com",
        "disabled": True,
        "password": "$2a$12$WSkiPnn4N7iuDSM7dIlmm.gIONFf1D14ARY.n87LjNy0f6ejgxPvK"
    },
    "kck": {
        "username": "kck",
        "name": "ick",
        "email": "ickkck@mail.com",
        "disabled": True,
        "password": "$2a$12$WSkiPnn4N7iuDSM7dIlmm.gIONFf1D14ARY.n87LjNy0f6ejgxPvK"
    }
}


def search_user(username: str):
    if username in user_db:
        return User(**user_db[username])
    
def search_user_db(username: str):
    if username in user_db:
        return UserDB(**user_db[username])


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Credenciales incorrectas",
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)

        

async def current_user(user: User = Depends(auth_user)):
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
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = {"sub": user.username, "exp": expire}
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user


















