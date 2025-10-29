from sqlmodel import SQLModel, Field

class Personal(SQLModel, table=True):
    DNI: int = Field(default=None, primary_key=True)
    nom: str
    cognom: str
    mail: str
    tarjeta: str
    departament: str