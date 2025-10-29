from sqlmodel import SQLModel, Field

class assistencia_pers(SQLModel, table=True):
    DNI_pers: str = Field(default=None, primary_key=True, foreign_key="personal.dni")
    id_horari: int = Field(default=None, foreign_key="horari.id")