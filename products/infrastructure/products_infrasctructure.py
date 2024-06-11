from models import response
from db.models.BPDataBase import Products
from db.connection import  Session
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError

def get_Allproducts():
    """
    Retrieves all products from the database.

    Returns:
        response.APIResponse: The API response containing the products.
    """
    try:
        session = Session()
        products = session.query(Products).filter(Products.active == True).all()
        session.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=response.APIResponse(
            message="An error occurred while fetching products",
            data=str(e),
            status="error",
            status_code=500
        ).__dict__)
    if products is None or len(products) == 0:
        raise HTTPException(status_code=404, detail=response.APIResponse(
            message="No products found",
            data=None,
            status="error",
            status_code=404
        ).__dict__)
    return response.APIResponse(
        message="Products returned successfully",
        data=[product.to_dict() for product in products],
        status="success",
        status_code=200
    ).__dict__