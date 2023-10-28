from pymongo import MongoClient
from bson import Binary  # Importa Binary desde bson
import certifi
import time
from informacion import username, password, mongo_uri

# Función para convertir una imagen en Binary
def image_to_binary(image_path):
    with open(image_path, 'rb') as f:
        return Binary(f.read())

# Función para insertar información en MongoDB con imágenes como BinData
def insert_information(_database, custom_id, nombres, apellidos, direccion, raza, sexo, edad, descripcion, estado, telefono, correo, image_path, image_fondo_path):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client[_database]
        collection = db["gatos"]  # Guardar todo en la colección "perros"
        
        # Convierte las imágenes a BinData
        imagen_bin = image_to_binary(image_path)
        imagen_fondo_bin = image_to_binary(image_fondo_path)
        
        # Crea un diccionario (documento) con los campos, incluyendo las imágenes como BinData
        document = {
            '_id': custom_id,
            'nombres': nombres,
            'apellidos': apellidos,
            'direccion': direccion,
            'raza': raza,
            'sexo': sexo,
            'edad': edad,
            'descripcion': descripcion,
            'estado': estado,
            'telefono': telefono,
            'correo': correo,
            'imagen': imagen_bin,  # Guarda la imagen como BinData
            'imagen_fondo': imagen_fondo_bin  # Guarda la imagen de fondo como BinData
        }
            
        # Inserta el documento con los campos y las imágenes como BinData
        collection.insert_one(document)
    except ConnectionError:
        print("Error de conexión con la base de datos")

# Rutas a tus imágenes locales
image_path = r'C:\Users\Luis\OneDrive\Documentos\Startup\PatitasyCariciasWeb\static\imgs\00000003.png'
image_fondo_path = r'C:\Users\Luis\OneDrive\Documentos\Startup\PatitasyCariciasWeb\static\imgs\fondo3.png'

# Llama a la función para insertar la información con las imágenes como BinData
insert_information("patitasycaricias",
                    "00000003",
                    "Chimuelo",
                    "Larco",
                    "San Borja. Cdra 13",
                    "Bengalí",
                    "Macho",
                    "3 meses",
                    "Juguetón y alegre",
                    "Perdido",
                    "+51 ---------",
                    "---------@gmail.com",
                    image_path,
                    image_fondo_path)
