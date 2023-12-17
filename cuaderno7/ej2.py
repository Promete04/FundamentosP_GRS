"""Realiza un programa que almacene 10 frases diferentes en una lista y nos
permita ordenar la misma de forma descendentemente utilizando como
criterio la longitud de la frase. Utiliza el método de inserción directa.
"""


def modificar_frases(lista):
    arr=[]
    for j in lista:
        arr.append([len(j),j])

    return arr

def odenar_frasecitas(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1]= key



lista = ["Hello", "world","kzjkvhzliv", "I", "am", "an", "AI","woawoawoawoaowoaowoaow","Alemania"]
arr = modificar_frases(lista)
odenar_frasecitas(arr)
print(arr)


