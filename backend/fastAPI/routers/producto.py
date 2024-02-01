from fastapi import APIRouter

router = APIRouter(prefix="/productos", 
                   responses={404: {"message": "No encontrado"}}, 
                   tags={"productos"})
"""
Con tags creas una sección en el apartado de documentacion de Swagger, 
en éste caso se crea la sección de productos.
"""

product_list = ["producto 1", "producto 2", "producto 3", "producto 4", "producto 5"]

@router.get("/") # Con prefix es como si hubiera "/productos" en la ruta del get
async def productos():
    return product_list


@router.get("/{id}") # Con prefix es como si hubiera "/productos/{id}" en la ruta del get
async def productos(id: int):
    return product_list[id]