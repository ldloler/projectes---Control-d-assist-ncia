from sqlmodel import SQLModel, Field

class Horari(SQLModel, table=True):
    ID: int = Field(default=None, primary_key=True)
    aula: str
    dia_setmana: str
    hora_inici: int
    hora_final: int