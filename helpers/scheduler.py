from _datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def scheduler_job(funcion, minutos,tarea_id, *args, **kwargs):
    try:
        run_time = datetime.now() + timedelta(minutes=minutos)
        scheduler.add_job(funcion, 'date', args=args, kwargs=kwargs, run_date=run_time, id=tarea_id)
        print(f'Tarea programada: {tarea_id}')
    except Exception as e:
        print(f'Error al programar la tarea: {e}')
        raise Exception(f'Error al programar la tarea: {e}')

def cancelar_tarea(tarea_id):
    try:
        scheduler.remove_job(tarea_id)
        return f'Tarea {tarea_id} cancelada'
    except Exception as e:
        raise Exception(f'Error al cancelar la tarea: {e}')
