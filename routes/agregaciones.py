##########################################
#               Bibliotecas
##########################################
from fastapi import APIRouter
import pandas as pd 
##########################################
#               Dependencias
##########################################
from config.database import db
from config.utilities import dataframe, dataframe2Dict

calculos = APIRouter(
    tags = ["Agregaciones de resultados"]
)

@calculos.get("/sexos")
async def obtener_sexos():
    """
    Permite calcular la cantidad y la proporcion 
    de sexos de los encuestados
    """
    # Obtenemos los sexos de la base de datos
    datos = list(db.encuesta.find({}, {"_id" : 0, "sexo" : 1}))
    # Convertimos a dataframe
    datos = pd.DataFrame(datos)
    # Calculamos la cantidad de encuestados por sexo
    sexos = datos.groupby(["sexo"]).size().reset_index(name = "cantidad")
    # OBtenemos la cantidad de encuestados
    n_datos = sexos["cantidad"].sum()
    # Calculamos la proporcion de sexos
    proporcion = sexos["cantidad"].values / n_datos
    # Añadimos esta nueva columna de datos
    sexos["proporcion"] = proporcion

    return(dataframe2Dict(sexos))