from sqlmodel import SQLModel, Field

class Professor(SQLModel, table=True):
    DNI: int = Field(default=None, primary_key=True)
    nom: str
    cognom: str
    mail: str
    tarjeta: str