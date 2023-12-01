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
"""para evitar calcularlo todo 10000 veces lo que hacemos es guardar los valores en un diccionariom memoizacion sin r"""

def fibonacci(n, cache={}):
    # Si el valor ya está en el cache, devuélvelo
    if n in cache:
        return cache[n]
    # Casos base
    elif n <= 1:
        result = n
    # Caso recursivo
    else:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    # Almacena el resultado en el cache antes de devolverlo
    cache[n] = result
    return result

"""Permutación
[]->[]
[x]->[x]
[x,y]->[x,y][x,x],[y,x][y,y]

"""

def hanoi(n, source, target, auxiliary):
    # Si todavía hay discos para mover
    if n > 0:
        # Primero, necesitamos mover los n - 1 discos superiores de la torre fuente a la torre auxiliar
        # Para hacer esto, tratamos la torre auxiliar como el objetivo y la torre objetivo como auxiliar
        hanoi(n - 1, source, auxiliary, target)

        # Una vez que los n - 1 discos superiores se han movido a la torre auxiliar, podemos mover el disco restante
        # (el más grande) de la torre fuente a la torre objetivo
        print(f'Move disk from tower {source} to tower {target}')

        # Finalmente, necesitamos mover los n - 1 discos que dejamos en la torre auxiliar a la torre objetivo
        # Para hacer esto, tratamos la torre fuente como auxiliar
        hanoi(n - 1, auxiliary, target, source)

# Prueba la función con 3 discos
# 'A' es la torre fuente, 'C' es la torre objetivo, y 'B' es la torre auxiliar
hanoi(3, 'A', 'C', 'B')


