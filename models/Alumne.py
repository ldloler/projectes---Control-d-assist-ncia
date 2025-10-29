from sqlmodel import SQLModel, Field

class Alumne(SQLModel, table=True):
    DNI: int = Field(default=None, primary_key=True)
    nom: str
    cognom: str
    mail: str
    tarjeta: str
    idalu: int