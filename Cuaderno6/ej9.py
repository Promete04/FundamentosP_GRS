"""Programar un algoritmo recursivo que obtenga la suma de las edades de todos
los elementos de una lista de alumnos. Un alumno está caracterizado por tres
atributos (nombre, edad, titulacion)."""

diccionario = {}
diccionario["alumno1"] = {"nombre": "Juan", "edad": 20, "titulacion": "Ingeniería Informática"}
diccionario["alumno2"] = {"nombre": "Ana", "edad": 22, "titulacion": "Matemáticas"}
...


def suma_edades(diccionario):
    if len(diccionario) == 0:
        return 0
    else:
        primera_llave = list(diccionario.keys())[0]
        primer_valor = diccionario[primera_llave]['edad']
        diccionario.pop(primera_llave)
        return primer_valor + suma_edades(diccionario)

print(suma_edades(diccionario))


