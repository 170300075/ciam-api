##########################################
#               Bibliotecas
##########################################
from fastapi import APIRouter

##########################################
#               Dependencias
##########################################
from config.database import db

##########################################
#               Dependencias
##########################################
from models.surveys import Survey

encuesta = APIRouter(
    tags = ["Resultados de encuesta"]
)

@encuesta.get("/resultados", response_model = list[Survey])
async def obtener_resultados():
    datos = list(db.encuesta.find({}, {"_id" : 0}))

    return(datos)