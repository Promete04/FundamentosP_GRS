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

def círculo(r: float) -> float:
    return pi * (r**2)


def areaTriangulo(b: float, h: float) -> float:
    return 0.5 * b * h


def areaCuadrado(b: float) -> float:
    return b**2


if tipo== "círculo": 
    r= float(input(f"Introduce el radio del {tipo}\n"))
    print(str(círculo(r))+" metros cuadrados")
elif tipo== "cuadrado":
    b= float(input(f"Introduce la base del {tipo}\n"))
    print (str(areaCuadrado(b))+" metros cuadrados")
else:
    h= float(input(f"Introduce la altura del {tipo}\n"))
    b= float(input(f"Introduce la base del {tipo}\n"))
    print (str(areaTriangulo(b,h))+" metros cuadrados")


