"""Una lista de enteros original debe utilizarse para generar dos listas, una con los
números pares de la original ordenados ascendentemente y otra con los impares
ordenados descendentemente. La generación de las 2 listas debe hacerse a
medida que se recorre la original, es decir, se toma un número de la original, se
decide a qué lista (pares o impares) debe ir, y se inserta ordenado en la misma
de acuerdo con el criterio de la lista (ascendente o descendente)."""



def ordenar_lista(lista):
    lista_pares = []
    lista_impares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
            lista_pares.sort()
        else:
            lista_impares.append(i)
            lista_impares.sort(reverse=True)
    return lista_pares, lista_impares   

print(ordenar_lista([1,2,3,4,5,6,7,8,9,10]))