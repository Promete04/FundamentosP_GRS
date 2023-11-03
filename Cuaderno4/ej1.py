"""Escribir una función que sume dos listas de enteros de igual longitud y retorne
otra lista que contenga la suma de las originales elemento a elemento."""

def sumar_listas(lista1, lista2):
        lista_suma = []
        for i in range(len(lista1)):
            lista_suma.append(lista1[i] + lista2[i])
        return lista_suma

print(sumar_listas([1,2,3],[4,5,6]))