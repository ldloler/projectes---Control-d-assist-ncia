from models.Curs import Curs
from schemas.Curs_schema import cursos_schema
from sqlmodel import Session, select

# Llegeix tots els Cursos de la BBDD.
def get_all_cursos(db):
    sql_read = select(Curs)
    cursos = db.exec(sql_read).all()
    return cursos_schema(cursos)

# Crea un Curs a la BBDD.
def save_curs(curs: Curs, db: Session):
    db.add(curs)
    db.commit()
    db.refresh(curs)
    return curs

# Elimina un Curs de la BBDD.
def del_curs(id, db:Session):
    try:
        statement = select(Curs).where(Curs.ID == id)
        results = db.exec(statement)
        client = results.one()
        db.delete(client)
        db.commit()
        return 1
    except:
        return 0