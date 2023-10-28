from pymongo import MongoClient
import certifi
import time
from informacion import username, password, mongo_uri


def createDatabaseCollection(_database,_collection):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client[_database]  # Esto apunta a la base de datos, pero no la crea aún
        collection = db[_collection]  # Esto apunta a una colección en la base de datos
        # Ahora puedes realizar alguna operación, como la inserción de datos
        collection.insert_one({"key": "value"})
    except ConnectionError:
        print("Error de conexión con la base de datos")

# Llama a la función para crear la base de datos
# createDatabaseCollection("mydatabase","mycollection")


def insert(_database, _collection, custom_id, _key, _value):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client[_database]
        collection = db[_collection]
            
        # Crea un diccionario (documento) con el campo '_id' personalizado y otros campos
        document = {
            '_id': custom_id,
            _key: _value
        }
            
        # Inserta el documento con el '_id' personalizado y otros campos
        collection.insert_one(document)
    except ConnectionError:
        print("Error de conexión con la base de datos")

def update(_database, _collection, custom_id, _key, _value):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client[_database]
        collection = db[_collection]
            
        document = {
            '_id': custom_id,
            _key: _value
        }
            
        collection.update_one({'_id': custom_id}, {'$set': {_key:_value}})
    except ConnectionError:
        print("Error de conexión con la base de datos")

insert("mydatabase", "mycollection", "001", "nombre", "Luis")
   
