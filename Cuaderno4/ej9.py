"""Implemente una función que indique si una palabra contiene las cinco vocales:
por ejemplo “murciélago”. Modifique posteriormente la función para que detecte
sólo aquellas palabras que contienen una única vez cada vocal."""

def vocales(palabra:str)->bool:
    resultado= False
    vocales= "aeiuo"
    aux=0
    for vocal in vocales:
        if vocal in palabra:
            aux +=1
    if aux >= 5:
        resultado= True
    return resultado

def vocales2(palabra:str)->bool:
    vocales= "aeiou"
    resultado= False
    aux= 0
    for vocal in vocales:
        if palabra.count(vocal) == 1:
            aux +=1
        if aux == 5:
            resultado= True
    return resultado

print(vocales("hola"))
print(vocales2("hola"))
print(vocales("murcielago"))
print(vocales2("murcielago"))
print(vocales2("murcielagoo"))