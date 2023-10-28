from flask import Flask, render_template, request, Response, jsonify, redirect, url_for, send_file
from pymongo import MongoClient
import certifi
import base64
from bson import ObjectId
from bson.binary import Binary
from informacion import username, password, mongo_uri
from product_mascota import Product
import database_mascota as dbase

db = dbase.dbConnection()
app = Flask(__name__)

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
            print(f'facebook: {document["facebook"]}')
            print(f'instagram: {document["instagram"]}')
            print(f'tiktok: {document["tiktok"]}')
            print(f'imagen: {document["imagen"]}')
            print(f'imagen_fondo: {document["imagen_fondo"]}')
        else:
            print("Documento no encontrado.")
    except ConnectionError:
        print("Error de conexión con la base de datos")

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/mascotas')
def mascotas():
    return render_template('mascotas.html')

@app.route('/perros')
def perros():
    client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
    db = client["patitasycaricias"]
    collection = db["perros"]

    documents = collection.find()  # Recupera todos los documentos de la colección

    # Convierte los datos binarios en cadenas base64 para cada documento
    data_list = []
    for document in documents:
        image_base64 = base64.b64encode(document["imagen"]).decode("utf-8")
        image_fondo_base64 = base64.b64encode(document["imagen_fondo"]).decode("utf-8")
        data_list.append({
            'document': document,
            'image_base64': image_base64,
            'image_fondo_base64': image_fondo_base64
        })

    return render_template('perros.html', data_list=data_list)

@app.route('/gatos')
def gatos():
    client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
    db = client["patitasycaricias"]
    collection = db["gatos"]

    documents = collection.find()  # Recupera todos los documentos de la colección

    # Convierte los datos binarios en cadenas base64 para cada documento
    data_list = []
    for document in documents:
        image_base64 = base64.b64encode(document["imagen"]).decode("utf-8")
        image_fondo_base64 = base64.b64encode(document["imagen_fondo"]).decode("utf-8")
        data_list.append({
            'document': document,
            'image_base64': image_base64,
            'image_fondo_base64': image_fondo_base64
        })

    return render_template('gatos.html', data_list=data_list)


@app.route('/perro/<custom_id>')
def perro(custom_id):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client["patitasycaricias"]
        collection = db["perros"]

        document = collection.find_one({'_id': custom_id})
        # Convierte los datos binarios en cadenas base64
        image_base64 = base64.b64encode(document["imagen"]).decode("utf-8")
        image_fondo_base64 = base64.b64encode(document["imagen_fondo"]).decode("utf-8")


        if document:
            return render_template('perro_template.html', data=document, image=image_base64, image_fondo=image_fondo_base64)
        else:
            return "Documento no encontrado."

    except ConnectionError:
        return "Error de conexión con la base de datos"

@app.route('/gato/<custom_id>')
def gato(custom_id):
    try:
        client = MongoClient(mongo_uri(), tlsCAFile=certifi.where())
        db = client["patitasycaricias"]
        collection = db["gatos"]

        document = collection.find_one({'_id': custom_id})
        # Convierte los datos binarios en cadenas base64
        image_base64 = base64.b64encode(document["imagen"]).decode("utf-8")
        image_fondo_base64 = base64.b64encode(document["imagen_fondo"]).decode("utf-8")


        if document:
            return render_template('gato_template.html', data=document, image=image_base64, image_fondo=image_fondo_base64)
        else:
            return "Documento no encontrado."

    except ConnectionError:
        return "Error de conexión con la base de datos"

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


# REGISTRO DE PERROS

@app.route('/actualizar_perro')
def actualizar_perro():
    products = db['perros']
    productsReceived = products.find()
    return render_template('actualizar_perro.html', products = productsReceived)

@app.route('/registro_perro')
def registro_perro():
    products = db['perros']
    productsReceived = products.find()
    return render_template('registro_perro.html', products = productsReceived)

# Ruta para mostrar la imagen
@app.route('/images/<string:image_id>', methods=['GET'])
def get_image(image_id):
    products = db['perros']
    product = products.find_one({'_id': image_id})

    if product and 'imagen' in product:
        image_data = product['imagen']
        print("Longitud de los datos de la imagen:", len(image_data))  # Imprime la longitud de los datos de la imagen
        return Response(image_data, content_type='image/jpeg')  # Ajusta el tipo de contenido según el formato de la imagen

    return "Imagen no encontrada"


# method post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['perros']
    _id = request.form['_id']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    direccion = request.form['direccion']
    raza = request.form['raza']
    sexo = request.form['sexo']
    edad = request.form['edad']
    descripcion = request.form['descripcion']
    estado = request.form['estado']
    telefono = request.form['telefono']
    correo = request.form['correo']
    facebook = request.form['facebook']
    instagram = request.form['instagram']
    tiktok = request.form['tiktok']
    imagen = request.files['imagen']
    imagen_fondo = request.files['imagen_fondo']

    if _id and nombres and apellidos and direccion and raza and sexo and edad and descripcion and estado and telefono and correo and facebook and instagram and tiktok and imagen and imagen_fondo:
        product = Product( _id, nombres, apellidos, direccion, raza, sexo, edad, descripcion, estado, telefono, correo, facebook, instagram, tiktok, imagen.read(), imagen_fondo.read()) # Lee la imagen y guárdala en el campo binario
        products.insert_one(product.toDBCollection())
        response = jsonify({
            '_id': _id,
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
            'facebook': facebook,
            'instagram': instagram,
            'tiktok': tiktok,
            'imagen': imagen.filename,
            'imagen_fondo': imagen_fondo.filename
        })
        return redirect(url_for("registro_perro"))
    else:
        return notFound()


# method delete
@app.route('/delete/<string:product_id>')
def delete(product_id):
    products = db['perros']
    products.delete_one({
        '_id': product_id
    })
    return redirect(url_for("actualizar_perro"))


# method put
@app.route('/edit/<string:product_id>', methods=['POST']) #recomendable pasar el id
def edit(product_id):
    products = db['perros']
    _id = request.form['_id']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    direccion = request.form['direccion']
    raza = request.form['raza']
    sexo = request.form['sexo']
    edad = request.form['edad']
    descripcion = request.form['descripcion']
    estado = request.form['estado']
    telefono = request.form['telefono']
    correo = request.form['correo']
    facebook = request.form['facebook']
    instagram = request.form['instagram']
    tiktok = request.form['tiktok']

    if _id and nombres and apellidos and direccion and raza and sexo and edad and descripcion and estado and telefono and correo and facebook and instagram and tiktok:
        products.update_one({'_id': product_id}, {'$set': {'nombres':nombres,'apellidos':apellidos, 'direccion':direccion, 'raza': raza, 'sexo':sexo, 'edad':edad, 'descripcion':descripcion, 'estado':estado, 'telefono':telefono, 'correo':correo, 'facebook': facebook, 'instagram': instagram, 'tiktok':tiktok}})
        response = jsonify({'message':'Información de mascota: ' + product_id +  'actualizado correctamente'})
        return redirect(url_for("actualizar_perro"))
    else:
        return notFound()


# REGISTRO DE GATOS

@app.route('/actualizar_gato')
def actualizar_gato():
    products = db['gatos']
    productsReceived = products.find()
    return render_template('actualizar_gato.html', products = productsReceived)

@app.route('/registro_gato')
def registro_gato():
    products = db['gatos']
    productsReceived = products.find()
    return render_template('registro_gato.html', products = productsReceived)

# Ruta para mostrar la imagen
@app.route('/imagesGatos/<string:image_id>', methods=['GET'])
def get_imageGatos(image_id):
    products = db['gatos']
    product = products.find_one({'_id': image_id})

    if product and 'imagen' in product:
        image_data = product['imagen']
        print("Longitud de los datos de la imagen:", len(image_data))  # Imprime la longitud de los datos de la imagen
        return Response(image_data, content_type='image/jpeg')  # Ajusta el tipo de contenido según el formato de la imagen

    return "Imagen no encontrada"


# method post
@app.route('/productsGatos', methods=['POST'])
def addProductGatos():
    products = db['gatos']
    _id = request.form['_id']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    direccion = request.form['direccion']
    raza = request.form['raza']
    sexo = request.form['sexo']
    edad = request.form['edad']
    descripcion = request.form['descripcion']
    estado = request.form['estado']
    telefono = request.form['telefono']
    correo = request.form['correo']
    facebook = request.form['facebook']
    instagram = request.form['instagram']
    tiktok = request.form['tiktok']
    imagen = request.files['imagen']
    imagen_fondo = request.files['imagen_fondo']

    if _id and nombres and apellidos and direccion and raza and sexo and edad and descripcion and estado and telefono and correo and facebook and instagram and tiktok and imagen and imagen_fondo:
        product = Product( _id, nombres, apellidos, direccion, raza, sexo, edad, descripcion, estado, telefono, correo, facebook, instagram, tiktok, imagen.read(), imagen_fondo.read()) # Lee la imagen y guárdala en el campo binario
        products.insert_one(product.toDBCollection())
        response = jsonify({
            '_id': _id,
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
            'facebook': facebook,
            'instagram': instagram,
            'tiktok': tiktok,
            'imagen': imagen.filename,
            'imagen_fondo': imagen_fondo.filename
        })
        return redirect(url_for("registro_gato"))
    else:
        return notFound()


# method delete
@app.route('/deleteGatos/<string:product_id>')
def deleteGatos(product_id):
    products = db['gatos']
    products.delete_one({
        '_id': product_id
    })
    return redirect(url_for("actualizar_gato"))


# method put
@app.route('/editGatos/<string:product_id>', methods=['POST']) #recomendable pasar el id
def editGatos(product_id):
    products = db['gatos']
    _id = request.form['_id']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    direccion = request.form['direccion']
    raza = request.form['raza']
    sexo = request.form['sexo']
    edad = request.form['edad']
    descripcion = request.form['descripcion']
    estado = request.form['estado']
    telefono = request.form['telefono']
    correo = request.form['correo']
    facebook = request.form['facebook']
    instagram = request.form['instagram']
    tiktok = request.form['tiktok']

    if _id and nombres and apellidos and direccion and raza and sexo and edad and descripcion and estado and telefono and correo and facebook and instagram and tiktok:
        products.update_one({'_id': product_id}, {'$set': {'nombres':nombres,'apellidos':apellidos, 'direccion':direccion, 'raza': raza, 'sexo':sexo, 'edad':edad, 'descripcion':descripcion, 'estado':estado, 'telefono':telefono, 'correo':correo, 'facebook': facebook, 'instagram':instagram, 'tiktok':tiktok}})
        response = jsonify({'message':'Información de mascota: ' + product_id +  'actualizado correctamente'})
        return redirect(url_for("actualizar_gato"))
    else:
        return notFound()


@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado '+ request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
