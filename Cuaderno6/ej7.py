"""Realizar un programa que lea desde teclado un número entero positivo y lo
convierta a binario utilizando recursividad."""

def pasar_a_binario (n:int)->int:
    if n<2:
        return n
    else:
        return pasar_a_binario(n//2)*10+n%2
    

n = int(input("Introduce un número entero positivo "))
print(pasar_a_binario(n))