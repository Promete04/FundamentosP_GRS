"""Programar, haciendo uso de la recursividad, una función en Python que
permita obtener el término de orden n de la sucesión de Fibonacci
(https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci) """

def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)