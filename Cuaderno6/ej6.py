"""Realizar una función recursiva que dado un número entero, cuente su número
de dígitos. Por ejemplo, si el número es 235, deberá retornar 3."""

def contar_digitos(n: int) -> int:
    if n<10:
        result = 1
    else:
        result = 1 + contar_digitos(n//10)