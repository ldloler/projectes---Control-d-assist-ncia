import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from services import curs as curs_service
from models.Curs import Curs as Curs_model
from schemas import Curs_schema


# Creació de FastAPI
app = FastAPI()

# Carregar variables d'entorn
load_dotenv()

# Obtenir variable d'entorn
DATABASE_URL = os.getenv("DATABASE_URL")
# Crear engine per la gestió de la DB
engine = create_engine(DATABASE_URL)

# Crear automàticament les taules a la bbdd
SQLModel.metadata.create_all(engine)

# Afegim middleware. (Perquè el frontend pugui treballar amb les dades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtenir sessió de la Base de Dades
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# ###############
# Cursos
# ###############

# Llegeix tots els cursos.
@app.get("/cursos/", response_model=list[dict])
async def read_cursos(db: Session = Depends(get_db)):
    result = curs_service.get_all_cursos(db)
    return result

# Guarda un curs a la db.
@app.put("/cursos/", response_model=str)
async def save_curs(curs: Curs_model, db: Session = Depends(get_db)):
    curs = curs_service.save_curs(curs, db)
    return '1 curs afegit' if curs != None else '0 cursos afegits'

# Borrar un curs de la db.
@app.delete("/cursos/{id_curs}", response_model=str)
async def del_curs(id_curs: int, db: Session = Depends(get_db)):
    numReg = curs_service.del_curs(id_curs, db)
    return f'{numReg} cursos eliminats'

# Llegeix 1 curs a la db. Segons id
@app.get("/cursos/{id_curs}", response_model=list[dict])
async def read_1_cursos(id_curs: int, db: Session = Depends(get_db)):
    result = curs_service.get_1_cursos(id_curs, db)
    return result