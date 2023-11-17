"""Implementar una función que pone en mayúsculas la primera letra de cada una
de las palabras de una frase, sin usar el método title()."""

def mayus(palabra:str)->str:
    lista = palabra.split()
    for i in range(len(lista)): 
        lista[i] = lista[i].capitalize()
    return " ".join(lista)

print(mayus("hola mundo"))