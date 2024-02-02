from fastapi import FastAPI
from routers import producto, users, oauth2_users, oauth_jwt_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

"""APIrouter para incluir el resto de API al main y levantar solo 1 fichero para varias API"""
app.include_router(producto.router)
app.include_router(users.router)
app.include_router(oauth2_users.router) # Comentar para mas seguridad, oauth_jwt_users descomentado
#app.include_router(oauth_jwt_users.router) # Descomentar para mas seguridad, oauth2 comentado
app.include_router(users_db.router)

"""Incluir fichero estaticos al API, directory indica donde se encuentra los recursos, 
el primer str indica el nombre del string que aparecen en la ruta para llegar al directorio,
el name si no lo se"""
app.mount("/static", StaticFiles(directory="CDN"), name="/static")

@app.get("/")
async def root():
    return "Hello world!!"

@app.get("/url")
async def url():
    return {"url":"www.google.es"}









