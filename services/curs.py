from models.Curs import Curs
from schemas.Curs_schema import cursos_schema
from sqlmodel import Session, select

# Llegeix tots els Cursos de la BBDD.
def get_all_cursos(db: Session):
    sql_read = select(Curs)
    cursos = db.exec(sql_read).all()
    return cursos_schema(cursos)

# Llegeix 1 Curs de la BBDD. Segons id.
def get_1_cursos(id, db: Session):
    sql_read = select(Curs).where(Curs.ID == id)
    result = db.exec(sql_read)
    curs = result.all()
    return cursos_schema(curs)

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