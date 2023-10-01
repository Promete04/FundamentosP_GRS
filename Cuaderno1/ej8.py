"""Escribe un programa que, a partir de los lados de un rectángulo, calcule su
área y perímetro y los muestre por pantalla."""


base = int(input("Cuantos metros mide la base del rectángulo?\n"))
altura = int(input("Cuantos  metros mide de altura el rectángulo?\n"))

perímetro = 2*base + 2*altura
area = base*altura

print(f"El rectángulo tiene un perímetro de {perímetro} metros\nEl rectángulo tiene un área de {area} metros cuadrados")