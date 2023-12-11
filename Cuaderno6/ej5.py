"""Programar una función que dada una palabra, retorne la misma invertida
utilizando para ello recursividad."""

def invertir_palabra(palabra: str) -> str:
    if len(palabra) == 1:
        return palabra
    else:
        return palabra[-1] + invertir_palabra(palabra[:-1])
    

palabra = "hola"
print(invertir_palabra(palabra))