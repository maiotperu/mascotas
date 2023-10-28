from bson.binary import Binary

class Product:
    def __init__(self, _id, nombres, apellidos, direccion, raza, sexo, edad, descripcion, estado, telefono, correo, facebook, instagram, tiktok, imagen, imagen_fondo):
        self._id = _id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.descripcion = descripcion
        self.estado = estado
        self.telefono = telefono
        self.correo = correo
        self.facebook = facebook
        self.instagram = instagram
        self.tiktok = tiktok
        self.imagen = Binary(imagen)
        self.imagen_fondo = Binary(imagen_fondo)


    def toDBCollection(self):
        return{
            '_id':self._id,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'direccion': self.direccion,
            'raza': self.raza,
            'sexo': self.sexo,
            'edad': self.edad,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'telefono': self.telefono,
            'correo': self.correo,
            'facebook': self.facebook,
            'instagram': self.instagram,
            'tiktok': self.tiktok,
            'imagen': self.imagen,
            'imagen_fondo': self.imagen_fondo
        }