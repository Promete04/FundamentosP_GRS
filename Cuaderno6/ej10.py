"""Dado un número en base decimal y una base menor que diez, escribir un
programa que cambie dicho número a la base dada utilizando para ello un
procedimiento recursivo."""

def cambiar_base(n: int, base: int) -> int:
    if n==1:
        result = base//2
    

#continuar con los casos base

print(cambiar_base(10, 2))  
print(cambiar_base(100, 8)) 
print(cambiar_base(17, 3))





