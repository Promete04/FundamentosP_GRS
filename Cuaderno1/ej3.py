"""Calcula y muestra por pantalla el área de un cuadrado:
a) Utilizando dos variables, una para almacenar la longitud del lado y
otra para almacenar el área.
b) Utilizando una única variable para almacenar la longitud del lado.
"""

Longitud_lado_a = int(input("Longitud del lado a:\n"))
Area = Longitud_lado_a**2
print(f"El area es igual a {Area} metros cuadrados")


Longitud_lado_b = int(input("Longitud del lado b:\n"))
print(f"El area es igual a {2*Longitud_lado_b} metros cuadrados")