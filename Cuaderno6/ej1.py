"""Programar un procedimiento recursivo que compruebe si un cierto número se
encuentra o no en una lista."""

def esta_en_lista(lista:list, num:int)->bool:
    encontrado = False
    if lista == []:
        encontrado = False
    elif lista[0] == num:
        encontrado = True
    else:
        encontrado= esta_en_lista(lista[1:],num)
    return encontrado

print(esta_en_lista([8,9,10],999))
        
    






