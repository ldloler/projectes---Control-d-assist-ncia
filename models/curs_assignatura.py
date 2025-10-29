from sqlmodel import SQLModel, Field

class curs_assignatura(SQLModel, table=True):
    id_curs: int = Field(default=None, primary_key=True, foreign_key="curs.id")
    id_assignatura: int = Field(default=None, primary_key=True, foreign_key="assignatura.id")
    DNI_professor: str = Field(default=None, foreign_key="professor.dni")