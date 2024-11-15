from fastapi import FastAPI
from bd_biblioteca import libros

app = FastAPI()

#Metodo: GET
#URL; '/'
@app.get('/')
def bienvenida():
    print("Atendiendo GET / ")
    respuesta = {"mensaje": "Bienvenido"}
    return respuesta

#Metodo Get
#URL '/libros'
#devuelva la lista de libros
@app.get('/libros')
def lista_libros():
    print("Atendiendo GET '/libros'")
    respuesta = libros
    return respuesta

#Metodo GET
#URL '/libros/{id}'
#devuelve un json
#parametro de ruta id
@app.get('/libros/{id}')
def informacion_libro(id:int):
    print("Atendiendo GET /libros/",id)
    if id >=0 and id <=len(libros)-1:
        respuesta = libros[id]
    else:
        respuesta = {
            "mensaje":"El libro no existe"
        }
    return respuesta