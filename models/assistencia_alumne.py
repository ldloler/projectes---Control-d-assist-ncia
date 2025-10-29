from sqlmodel import SQLModel, Field

class assistencia_alumne(SQLModel, table=True):
    DNI_alum: str = Field(default=None, primary_key=True, foreign_key="alumne.dni")
    id_horari: int = Field(default=None, primary_key=True, foreign_key="horari.id")
    id_curs: int = Field(default=None, foreign_key="curs_assignatura.id_curs")
    id_assignatura: int = Field(default=None, foreign_key="curs_assignatura.id_assignatura")