##########################################
#               Bibliotecas
##########################################
import pandas as pd
import requests
import json

##########################################
#               Dependencias
##########################################
from config.database import base_url

# Funciones de utilería
def dataframe2Dict(dataframe):
    """
    Esta funcion permite convertir un dataframe a
    un diccionario (JSON like)
    """
    # Convertir una dataframe a un diccionario
    data_dict = dataframe.to_dict("records")
    # Retornamos el diccionario
    return(data_dict)

def get(endpoint = ""):
    # En caso de deploy, cambiar por ruta de producción
    root = base_url

    res = requests.get(root + endpoint)
    res = json.loads(res.text)
    return(res)

def dataframe(endpoint = ""):
    df = pd.DataFrame(get(endpoint))
    return(df)