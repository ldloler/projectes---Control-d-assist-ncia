from models.Alumne import Alumne
from schemas.Alumne_schema import alumns_schema, alumn_schema
from sqlmodel import Session, select

# Llegeix tots els Alumnes de la BBDD.
def get_all_alumnes(db: Session):
    sql_read = select(Alumne)
    alumns = db.exec(sql_read).all()
    return alumns_schema(alumns)

# Crea un alumne a la BBDD.
def save_alumne(alumn: Alumne, db: Session):
    db.add(alumn)
    db.commit()
    db.refresh(alumn)
    return alumn

'''
# Llegeix 1 Curs de la BBDD. Segons id.
def get_1_cursos(id, db: Session):
    sql_read = select(Curs).where(Curs.ID == id)
    result = db.exec(sql_read)
    curs = result.all()
    return cursos_schema(curs)

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
def update_curs_full(id, new_curs: Curs, db: Session):
    sql_read = select(Curs).where(Curs.ID == id)
    result = db.exec(sql_read)
    curs = result.one()
    
    curs.nom = new_curs.nom
    curs.grup = new_curs.grup
    curs.promocio = new_curs.promocio

    # curs = Curs(ID=None, nom=curs.nom, grup=curs.grup, promocio=curs.promocio)

    curs = curs_schema(curs)

    db.add(curs)
    db.commit()
    db.refresh(curs)
    return curs
'''