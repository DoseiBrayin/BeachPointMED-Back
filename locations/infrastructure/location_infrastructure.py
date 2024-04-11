from models import response
from locations.models import locationModel
from db.connection import  Session
def get_locations() -> response.APIResponse:
    """
    Retrieves all locations from the database.

    Returns:
        response.APIResponse: The API response containing the locations.
    """
    try:
        # Create a session object
        session = Session()
        locations = session.query(locationModel.Location).filter(locationModel.Location.active == True).all()
        session.close()
        if not locations:
            return response.APIResponse(
                message="No locations found",
                data=None,
                status="success",
                status_code=404
            )
        return response.APIResponse(
            message="Locations returned successfully",
            data=[location.to_dict() for location in locations],
            status="success",
            status_code=200
        )
    except Exception as e:
        return response.APIResponse(
            message="An error occurred while fetching locations",
            data=None,
            status="error",
            status_code=500
        )