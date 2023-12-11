"""Calcular la suma de los números pares entre 0 y n de manera recursiva"""


def sum_even_numbers(n:int):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return n + sum_even_numbers(n-2)
    else:
        return sum_even_numbers(n-1)

n=2
print(sum_even_numbers(n))