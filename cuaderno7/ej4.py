"""Realiza un programa para gestionar los datos de stock de una tienda de
comestibles. La información a recoger será: nombre de producto, precio y
cantidad de stock. La tienda dispone de 10 productos distintos. El programa
debe ser capaz de:
    a. Dar de alta un producto nuevo
    b. Buscar un producto por su nombre, empleando búsqueda secuencial.
    c. Ordenar los productos por el método de la burbuja según su precio.
"""

def crear_almacen()->dict:
    almacen={}
    return almacen

def añadir_producto(almacen:dict,nombre:str,precio:float,cantidad:int):
    """numero= input("cuantos productos quieres añadir")
    .. el for _ in numero...
        nombre= input("Cual es el nombre del producto a añadir? ")
        precio= int(input("Cual es el precio del producto a añadir? "))
        cantidad= int(input("Cual es la cantidad del producto a añadir? "))""" 
    #lo quito para hacer más sencillo la introduccion de ejemplos
    producto = {"precio":precio,"stock":cantidad}
    almacen.update({nombre:producto})

def buscar_producto(almacen:dict, nombre_producto:str):
    bot=0
    top=len(almacen)-1
    mid = (bot+top)//2
    encontrado = False
    aux= 0
    while not encontrado and bot <= top:
        







