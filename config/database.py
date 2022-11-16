##########################################
#               Bibliotecas
##########################################
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargamos variables de ambiante
load_dotenv(".env")

# Leemos las credenciales de bases de datos
mongodb_uri = os.getenv("mongodb_uri")
# Leemos la url base de la API
base_url = os.getenv("base_url")

print("mongodb_uri: " + mongodb_uri)
print("base_url: " + base_url)

# Creamos una instancia con al base de datos
client = MongoClient(mongodb_uri)
db = client["ciam"]