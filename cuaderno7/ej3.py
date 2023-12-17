"""Modifica el programa anterior para que ordene en función del número de
palabras que hay en la frase. Usa ahora el método de selección directa. Pista:
será útil utilizar la función split()
"""


def selection_sort(a):
    for i in range(len(a)):
        max_idx = i
        for j in range(i+1, len(a)):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

def modificar_frases(lista):
    a=[]
    for j in lista:
        a.append([len(j),j])

    return a

lista = ["Hello", "world","kzjkvhzliv", "I", "am", "an", "AI","woawoawoawoaowoaowoaow","Alemania"]
a = modificar_frases(lista)
selection_sort(a)
print(a)
