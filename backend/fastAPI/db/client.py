from pymongo import MongoClient

"""DDBB local"""
db_client = MongoClient().local
"""
Si no se indica nada se conecta a la DDBB local
local es la instancia de la base de datos sobre la que se trabaja
"""


"""DDBB remota"""
# db_client = MongoClient("url").test
"""
La url viene proporcionada por la pagina web de la DDBB remota,
en el caso de MongoDB Atlas: Connect > Connect your application >
> Driver = Python > Version = {version de python utilizada} >
> Copiar el link que proporciona
test es sobre la base de datos en la que trabaja, en este caso se ha creado la DDBB test.
"""





















