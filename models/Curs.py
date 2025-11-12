from sqlmodel import SQLModel, Field

class Curs(SQLModel, table=True):
    ID: int = Field(default=None, primary_key=True)
    nom: str
    grup: str
    promocio: int

class Curs_modify_all(SQLModel):
    nom: str
    grup: str
    promocio: int