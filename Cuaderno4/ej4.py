"""Crear una lista de enteros, inicializarlos según valores aleatorios en el rango 1..20
y computar la media de los valores, el valor más alto y el más bajo (todo ello
utilizando listas). """

import random
def lista_aleatoria():
    lista = []
    for i in range(10):
        lista.append(random.randint(1,20))
    return lista

def media(lista):
    return sum(lista)/len(lista)

def maximo(lista):
    return max(lista)

def minimo(lista):
    return min(lista)

print(lista_aleatoria())
print(media(lista_aleatoria()))
print(maximo(lista_aleatoria()))
print(minimo(lista_aleatoria()))
