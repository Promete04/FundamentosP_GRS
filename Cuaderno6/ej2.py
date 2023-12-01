"""Implementar un programa que dados dos números, calcule el producto de
forma recursiva. Los números a multiplicar deben ser leídos por teclado.
NOTA: no puede utilizar el operador de multiplicación así que utilice sumas."""

x= float(input("Introduce el primer número "))
y= float(input("Introduce el segundo número "))

def sumo_pq_mult_es_tonto(x:int, y:int)->float:
    # Base case: if y is 0, the product is 0
    if y == 0 or x == 0:
        resultado= 0
    # Recursive case: add x to the product of x and (y-1)
    else:
        resultado= x + sumo_pq_mult_es_tonto(x, y-1)
    return resultado
# Call the function and print the result
print(sumo_pq_mult_es_tonto(x, y))