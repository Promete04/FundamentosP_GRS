"""Muy similar al anterior: Programar ahora un algoritmo recursivo que permita
hacer una división entera mediante restas sucesivas."""

def division_recursive(x: int, y: int) -> int:
    if y == 0:
        raise ValueError("Divisor cannot be zero")
    if x < y:
        return 0
    else:
        return 1 + division_recursive(x - y, y)

x = int(input("Introduce el dividendo "))
y = int(input("Introduce el divisor "))

try:
    print(division_recursive(x, y))
except ValueError as e:
    print(e)
