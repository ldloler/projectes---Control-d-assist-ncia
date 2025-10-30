from models.Curs import Curs
from schemas.Curs_schema import cursos_schema
from sqlmodel import Session, select

def get_all_cursos(db):
    sql_read = select(Curs)
    cursos = db.exec(sql_read).all()
    return cursos_schema(cursos)