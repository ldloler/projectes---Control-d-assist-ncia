from models.Curs import Curs, Curs_modify_all
from schemas.Curs_schema import cursos_schema, curs_schema
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
    
# Modifica completament 1 curs, segons id.
def update_curs_full(id, new_curs: Curs_modify_all, db: Session):
    sql_read = select(Curs).where(Curs.ID == id)
    result = db.exec(sql_read)
    curs = result.one()

    new_curs_data = new_curs.model_dump()
    curs.sqlmodel_update(new_curs_data)

    db.add(curs)
    db.commit()
    db.refresh(curs)
    return_curs = Curs(ID=curs.ID, nom=curs.nom, grup=curs.grup, promocio=curs.promocio)
    return return_curs

# Modifica nom de 1 curs, segons id.
def update_curs_nom(id, nom: str, db: Session):
    sql_read = select(Curs).where(Curs.ID == id)
    result = db.exec(sql_read)
    curs = result.one()
    
    curs.nom = nom

    db.add(curs)
    db.commit()
    db.refresh(curs)
    return curs

# Modifica grup de 1 curs, segons id.
def update_curs_grup(id, grup: str, db: Session):
    sql_read = select(Curs).where(Curs.ID == id)
    result = db.exec(sql_read)
    curs = result.one()
    
    curs.grup = grup

    db.add(curs)
    db.commit()
    db.refresh(curs)
    return curs