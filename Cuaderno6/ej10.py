"""Dado un número en base decimal y una base menor que diez, escribir un
programa que cambie dicho número a la base dada utilizando para ello un
procedimiento recursivo."""

def cambiar_base(n: int, base: int) -> int:
    if n < base:
        return n
    else:
        return cambiar_base(n//base, base)*10 + n%base
    
print(cambiar_base(10, 2))  # Expected output: 1010 (10 in base 2 is 1010)
print(cambiar_base(100, 8))  # Expected output: 144 (100 in base 8 is 144)
print(cambiar_base(17, 3))  # Expected output: 122 (17 in base 3 is 122)
