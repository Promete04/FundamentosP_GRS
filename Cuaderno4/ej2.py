""""Modifica la función anterior permitiendo que las listas sean desiguales. Los
elementos sobrantes de la lista más larga se añadirán al final de la lista
resultante."""

def suma_listas2(lista1,lista2):
    nueva_lista = []
    lista_corta = min(lista1, lista2, key=len)
    lista_larga = max(lista1, lista2, key=len)
    for i in range(len(lista_corta)):
        nueva_lista.append(lista_larga[i] + lista_corta[i])
    nueva_lista.extend(lista_larga[len(lista_corta):])
    return nueva_lista
print(suma_listas2([1,2,3],[4,5,6,7,8,9]))
        
        