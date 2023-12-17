"""Dado un número en base decimal y una base menor que diez, escribir un
programa que cambie dicho número a la base dada utilizando para ello un
procedimiento recursivo."""

def cambiar_base(numero: int, base_deseada: int) -> int:
    """Función que recibe un número en base decimal y una base menor que diez
    y devuelve el número en la base deseada.

    Args:
        numero (int): Número en base decimal.
        base_deseada (int): Base deseada.

    Returns:
        int: Número en la base deseada.
    """
    if numero < base_deseada:
        return numero
    else:
        return cambiar_base(numero // base_deseada, base_deseada) * 10 + (numero % base_deseada)

    
    
#continuar con los casos base

print(cambiar_base(1, 2)) 
print(cambiar_base(2, 2))
print(cambiar_base(3, 2))
print(cambiar_base(4, 2))
print(cambiar_base(5, 2))







