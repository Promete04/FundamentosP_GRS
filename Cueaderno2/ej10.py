""". Una aplicación leerá de teclado los valores necesarios para mostrar en
pantalla el área de un círculo, un cuadrado y un triángulo. No queremos
implementar la aplicación completa aún, sólo preparar los subprogramas de
que necesitaremos disponer para en un futuro construir la aplicación
(funciones que leen de teclado números y los validan, por una parte, y
funciones que hacen los cálculos de las distintas áreas, por otra). Nota: si lo
necesitas, utiliza como aproximación de П (pi) el valor de que proporciona la
biblioteca “math” de Python.
"""
import math

pi= math.pi

tipo = input("Que area quieres calcular? (círculo, cuadrado o triángulo)\n")

b= float(input("Introduce la base del {tipo}\n"))

h= float(input("Introduce la altura del triángulo\n"))

r= float(input("Introduce el radio del círculo\n"))

def círculo(r: float) -> float:
    return pi * (r**2)


def areaTriangulo(b: float, h: float) -> float:
    return 0.5 * b * h


def areaCuadrado(b: float) -> float:
    return b**2

