from sqlmodel import SQLModel, Field

class assistencia_prof(SQLModel, table=True):
    DNI_prof: str = Field(default=None, primary_key=True, foreign_key="professor.dni")
    id_horari: int = Field(default=None, foreign_key="horari.id")