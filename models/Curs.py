from sqlmodel import SQLModel, Field

class Curs(SQLModel, table=True):
    ID: int = Field(default=None, primary_key=True)
    nom: str
    grup: str
    promocio: int