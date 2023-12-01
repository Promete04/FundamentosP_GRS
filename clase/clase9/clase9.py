def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 2:
        return 1
    # Caso recursivo
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))

