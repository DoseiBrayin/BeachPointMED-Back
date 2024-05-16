from models import response
from timeCourts.models import timeCourts_model
from courts.models import courts_model
from db.connection import Session
from fastapi import HTTPException


def get_timeCourts(location: str) -> response.APIResponse:
    try:
        session = Session()
        timeCourts = session.query(
            timeCourts_model.Timecourts.id,
            timeCourts_model.Timecourts.fk_court,
            timeCourts_model.Timecourts.date,
            timeCourts_model.Timecourts.hour,
            timeCourts_model.Timecourts.price,
            timeCourts_model.Timecourts.state,
            courts_model.Courts.description,
        ).join(
            courts_model.Courts, timeCourts_model.Timecourts.fk_court == courts_model.Courts.id
        ).filter((courts_model.Courts.fk_location == location)
        ).order_by(timeCourts_model.Timecourts.date, timeCourts_model.Timecourts.hour
        ).all()
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


def get_timeCourts_by_date(date: str, location: str) -> response.APIResponse:
    try:
        session = Session()
        timeCourts = session.query(timeCourts_model.Timecourts.id,
            timeCourts_model.Timecourts.fk_court,
            timeCourts_model.Timecourts.date,
            timeCourts_model.Timecourts.hour,
            timeCourts_model.Timecourts.price,
            timeCourts_model.Timecourts.state,
            courts_model.Courts.description,).join(
                courts_model.Courts, timeCourts_model.Timecourts.fk_court == courts_model.Courts.id).filter(
                    (timeCourts_model.Timecourts.date == date)
                    & (courts_model.Courts.fk_location == location)
                    ).order_by(timeCourts_model.Timecourts.date).all()
        session.close()
        if not timeCourts:
            return response.APIResponse(
                message=f"There are no TimeCourts available on {date} in {location}",
                data=None,
                status="success",
                status_code=200,
            )
        timeCourts = [dict(row._asdict()) for row in timeCourts]
        timeCourts_pairs = []
        for a, b in zip(timeCourts[::2], timeCourts[1::2]):
            combined = {**a, **{f"{k}-2": v for k, v in b.items()}}
            combined.pop('date-2', None)
            combined.pop('hour-2', None)
            combined.pop('price-2', None)
            timeCourts_pairs.append(combined)
        if len(timeCourts) % 2:
            timeCourts_pairs.append(timeCourts[-1])
        return response.APIResponse(
            message="TimeCourts have been successfully retrieved",
            data=timeCourts_pairs,
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

def change_status_reserved(id):
    try:
        session = Session()
        timeCourt = session.query(timeCourts_model.Timecourts).filter(timeCourts_model.Timecourts.id == id).first()
        if timeCourt and timeCourt.state == 'Available':
            timeCourt.state = 'Reserved'
            session.commit()
            return response.APIResponse(
                message=f"TimeCourt {id} has been successfully reserved",
                data=None,
                status="success",
                status_code=200,
            )
        else:
            return response.APIResponse(
                message=f"TimeCourt {id} does not exist or is not available",
                data=None,
                status="success",
                status_code=404,
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=response.APIResponse(
            message="An error occurred while reserving the TimeCourt",
            data=str(e),
            status="error",
            status_code=500,
        ))
    finally:
        session.close()

def change_status_available(id):
    try:
        session = Session()
        timeCourt = session.query(timeCourts_model.Timecourts).filter(timeCourts_model.Timecourts.id == id).first()
        if timeCourt:
            timeCourt.state = 'Available'
            session.commit()
            return response.APIResponse(
                message=f"TimeCourt {id} has been successfully made available",
                data=None,
                status="success",
                status_code=200,
            )
        else:
            return response.APIResponse(
                message=f"TimeCourt {id} does not exist",
                data=None,
                status="success",
                status_code=404,
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=response.APIResponse(
            message="An error occurred while making the TimeCourt available",
            data=str(e),
            status="error",
            status_code=500,
        ))
    finally:
        session.close()

def change_status_unavailable(id):
    try:
        session = Session()
        timeCourt = session.query(timeCourts_model.Timecourts).filter(timeCourts_model.Timecourts.id == id).first()
        if timeCourt:
            timeCourt.state = 'Unavailable'
            session.commit()
            return response.APIResponse(
                message=f"TimeCourt {id} has been successfully made unavailable",
                data=None,
                status="success",
                status_code=200,
            )
        else:
            return response.APIResponse(
                message=f"TimeCourt {id} does not exist",
                data=None,
                status="success",
                status_code=404,
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=response.APIResponse(
            message="An error occurred while making the TimeCourt unavailable",
            data=str(e),
            status="error",
            status_code=500,
        ))
    finally:
        session.close()