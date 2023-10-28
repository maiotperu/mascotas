from pymongo import MongoClient
import certifi 
from informacion import username,password,mongo_uri

username = username()
password = password()
MONGO_URI = mongo_uri()

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["patitasycaricias"]
    except ConnectionError:
        print("Error de conexion con la bdd")
    return db

