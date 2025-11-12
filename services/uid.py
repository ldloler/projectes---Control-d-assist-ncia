import services.alumne as alum_service
from sqlmodel import Session

def check_uid(uid: str, db: Session):
    alumnos = alum_service.get_all_alumnes(db) 

    for alum in alumnos:
        if (alum.tarjeta == uid):
            return True

    return False