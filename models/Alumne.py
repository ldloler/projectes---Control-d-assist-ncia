from sqlmodel import SQLModel, Field

class Alumne(SQLModel, table=True):
    DNI: str = Field(default=None, primary_key=True)
    nom: str
    cognom: str
    mail: str
    tarjeta: str
    idalu: int