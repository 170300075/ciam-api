# FastAPI
from fastapi import FastAPI, HTTPException

# Descripción de la API
descripcion = """
CIAM API es una API REST que permite obtener la información de las encuestas
que se han realizado. Ademas, contempla una serie de endpoints que permite
obtener transformaciones de esos mismos datos para visualizarlas en el 
dashboard del CIAM.

CIAM API está desarrollado para hacer cosas maravillosas, hoy y en un futuro 🚀.
Hecho con ❤ por Kenneth a.k.a BlackMaster (170300075@ucaribe.edu.mx).
"""

from routes.encuesta import encuesta
from routes.agregaciones import calculos

# Crear una instancia de la API
app = FastAPI(
    title = "CIAM API",
    version = "1.0.0",
    description = descripcion,
    contact = {
        "name" : "Kenneth Díaz González",
        "email" : "kennethdiazgonzalez@hotmail.com"
    }
)

#######################################################
#              Endpoints de la API del CIAM           #
#######################################################
app.include_router(encuesta)
app.include_router(calculos)