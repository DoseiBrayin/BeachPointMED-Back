# controllers.py
from UserItem.models import user_model
from models import response
def get_item(item_id: int) -> user_model.Item:
    """
    Obtiene un item según su ID.

    Args:
        item_id (int): El ID del item a obtener.

    Returns:
        user_model.Item: El item obtenido.
    """
    # Aquí es donde normalmente interactuarías con la base de datos.
    # Como este es solo un ejemplo, vamos a devolver un item estático.
    return user_model.Item(name="Foo", description="A very nice Item", price=35.5)

def get_items() -> response.APIResponse:
    """
    Obtiene una lista de items.

    Returns:
        list[user_model.Item]: La lista de items.
    """
    # Aquí es donde normalmente interactuarías con la base de datos.
    # Como este es solo un ejemplo, vamos a devolver una lista de items estáticos.
    return response.APIResponse(
        message="Items have been successfully retrieved",
        data=[
            user_model.Item(name="Foo", description="A very nice Item", price=35.5),
            user_model.Item(name="Bar", description="Another very nice Item", price=45.5),
        ],
        status="success",
        status_code=200,
    )

def create_item(item: user_model.Item) -> user_model.Item:
    """
    Crea un nuevo item en la base de datos.

    Args:
        item (user_model.Item): El item a crear.

    Returns:
        user_model.Item: El item creado.
    """
    # Aquí es donde normalmente interactuarías con la base de datos.
    # Como este es solo un ejemplo, vamos a devolver el item que hemos creado.
    return item