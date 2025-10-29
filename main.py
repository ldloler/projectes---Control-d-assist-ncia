import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session


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