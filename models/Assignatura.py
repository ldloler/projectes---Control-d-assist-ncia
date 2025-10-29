from sqlmodel import SQLModel, Field

class Assignatura(SQLModel, table=True):
    ID: int = Field(default=None, primary_key=True)
    nom: str
    total_hores: int