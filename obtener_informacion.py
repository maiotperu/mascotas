from pymongo import MongoClient
import certifi
from bson.binary import Binary  # Importa Binary desde bson
from informacion import username, password, mongo_uri

def get_information(_database, custom_id):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client[_database]
        collection = db["perros"]  # Accede a la colección "perros"
        
        # Encuentra el documento con el _id personalizado
        document = collection.find_one({'_id': custom_id})
        
        # Imprime la información del documento
        if document:
            print(f'_id: {document["_id"]}')
            print(f'nombres: {document["nombres"]}')
            print(f'apellidos: {document["apellidos"]}')
            print(f'direccion: {document["direccion"]}')
            print(f'raza: {document["raza"]}')
            print(f'sexo: {document["sexo"]}')
            print(f'edad: {document["edad"]}')
            print(f'descripcion: {document["descripcion"]}')
            print(f'estado: {document["estado"]}')
            print(f'telefono: {document["telefono"]}')
            print(f'correo: {document["correo"]}')
            print(f'imagen: {document["imagen"]}')
            print(f'imagen_fondo: {document["imagen_fondo"]}')
        else:
            print("Documento no encontrado.")
    except ConnectionError:
        print("Error de conexión con la base de datos")

# Llama a la función para obtener e imprimir la información del documento
get_information("patitasycaricias", "00000001")
