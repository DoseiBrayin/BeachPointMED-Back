from models import response
from timeCourts.models import timeCourts_model
from courts.models import courts_model
from db.connection import  Session

def get_timeCourts(location:str) -> response.APIResponse:
    try:
        session = Session()
        timeCourts = session.query(
            timeCourts_model.Timecourts.id,
            timeCourts_model.Timecourts.fk_court,
            timeCourts_model.Timecourts.day,
            timeCourts_model.Timecourts.month,
            timeCourts_model.Timecourts.year,
            timeCourts_model.Timecourts.hour,
            timeCourts_model.Timecourts.price,
            courts_model.Courts.description,
            courts_model.Courts.state).join(
                courts_model.Courts, timeCourts_model.Timecourts.fk_court == courts_model.Courts.id).filter(
                    (courts_model.Courts.state == 'Available') 
                    & (courts_model.Courts.fk_location == location)).all()
        session.close()
        if not timeCourts:
            return response.APIResponse(
                message=f"There are no TimeCourts available in {location}",
                data=None,
                status="success",
                status_code=200,
            )
        timeCourts = [dict(row._asdict()) for row in timeCourts]
        return response.APIResponse(
            message="TimeCourts have been successfully retrieved",
            data=timeCourts,
            status="success",
            status_code=200,
        )
    except Exception as e:
        return response.APIResponse(
            message="An error occurred while retrieving the TimeCourts",
            data=str(e),
            status="error",
            status_code=500,
        )

def get_timeCourts_by_date(day:str, month:str, year:str,location:str) -> response.APIResponse:
    try:
        session = Session()
        timeCourts = session.query(
            timeCourts_model.Timecourts.id,
            timeCourts_model.Timecourts.fk_court,
            timeCourts_model.Timecourts.day,
            timeCourts_model.Timecourts.month,
            timeCourts_model.Timecourts.year,
            timeCourts_model.Timecourts.hour,
            timeCourts_model.Timecourts.price,
            courts_model.Courts.description,
            courts_model.Courts.state).join(
                courts_model.Courts, timeCourts_model.Timecourts.fk_court == courts_model.Courts.id).filter(
                    (timeCourts_model.Timecourts.day == day) 
                    & (timeCourts_model.Timecourts.month == month) 
                    & (timeCourts_model.Timecourts.year == year)
                    & (courts_model.Courts.fk_location == location)).all()
        session.close()
        if not timeCourts:
            return response.APIResponse(
                message=f"There are no TimeCourts available on {day}/{month}/{year}",
                data=None,
                status="success",
                status_code=200,
            )
        timeCourts = [dict(row._asdict()) for row in timeCourts]
        return response.APIResponse(
            message="TimeCourts have been successfully retrieved",
            data=timeCourts,
            status="success",
            status_code=200,
        )
    except Exception as e:
        return response.APIResponse(
            message="An error occurred while retrieving the TimeCourts",
            data=str(e),
            status="error",
            status_code=500,
        )
