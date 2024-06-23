from models import response
from db.connection import Session
from fastapi import HTTPException
from db.models.BPDataBase import Timecourts, Courts
from helpers.scheduler import scheduler_job

def get_timeCourts(location: str) -> response.APIResponse:
    try:
        session = Session()
        timeCourts = session.query(
            Timecourts.id,
            Timecourts.fk_court,
            Timecourts.date,
            Timecourts.hour,
            Timecourts.price,
            Timecourts.state,
           Courts.description,
        ).join(
           Courts, Timecourts.fk_court ==Courts.id
        ).filter((Courts.fk_location == location)
        ).order_by(Timecourts.date, Timecourts.hour
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
        timeCourts = session.query(Timecourts.id,
            Timecourts.fk_court,
            Timecourts.date,
            Timecourts.hour,
            Timecourts.price,
            Timecourts.state,
           Courts.description,).join(
               Courts, Timecourts.fk_court ==Courts.id).filter(
                    (Timecourts.date == date)
                    & (Courts.fk_location == location)
                    ).order_by(Timecourts.date).all()
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

def change_status_reserved(id, tarea_id):
    try:
        session = Session()
        states_courts = []
        for timeCourt_id in id:
            timeCourt = session.query(Timecourts).filter(Timecourts.id == timeCourt_id).first()
            if timeCourt and timeCourt.state == 'Available':
                timeCourt.state = 'Reserved'
                session.commit()
                states_courts.append(f'TimeCourt {timeCourt_id} has been successfully reserved')
            else:
                states_courts.append(f'TimeCourt {timeCourt_id} is not available to be reserved')
        print(states_courts)
        states_courts.append({"task_id": tarea_id, "message": "The task has been successfully completed"})
        return response.APIResponse(
            message="TimeCourts have been successfully reserved",
            data=states_courts,
            status="success",
            status_code=200,
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
        states_courts = []
        for timeCourt_id in id:
            timeCourt = session.query(Timecourts).filter(Timecourts.id == timeCourt_id).first()
            if timeCourt and timeCourt.state != 'Available':
                timeCourt.state = 'Available'
                session.commit()
                states_courts.append(f'TimeCourt {timeCourt_id} has been successfully made available')
            else:
                states_courts.append(f'TimeCourt {timeCourt_id} is available already')
        
        return response.APIResponse(
            message="TimeCourts have been successfully made available",
            data=states_courts,
            status="success",
            status_code=200,
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
        states_courts = []
        for timeCourt_id in id:
            timeCourt = session.query(Timecourts).filter(Timecourts.id == timeCourt_id).first()
            if timeCourt and timeCourt.state != 'Unavailable':
                timeCourt.state = 'Unavailable'
                session.commit()
                states_courts.append(f'TimeCourt {timeCourt_id} has been successfully made unavailable')
            else:
                states_courts.append(f'TimeCourt {timeCourt_id} is unavailable already')
        return response.APIResponse(
            message="TimeCourts have been successfully made unavailable",
            data=states_courts,
            status="success",
            status_code=200,
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