"""Modificar una lista de números reales que representan las calificaciones de los
alumnos de una clase, para sustituir los valores numéricos por sus calificaciones
alfanuméricas (Suspenso, Aprobado, etc.)"""

def calificaciones(lista):
    for i in range(len(lista)):
        if lista[i] < 5:
            lista[i] = "Suspenso"
        else:
            lista[i] = "Aprobado"
    return lista

print(calificaciones([1,2,3,4,5,6,7,8,9,10]))