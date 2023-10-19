"""Escribe un algoritmo que tras leer tres enteros los escriba en pantalla en orden
creciente. Como siempre, valida las entradas."""

n= input("Primer número")
x= input("Segundo número")
y= input("Tercer número")

def ordenar(n,x,y):
    try:
        int(n)  # Intenta convertir la entrada a un entero
        int(x)
        int(y)
        notas= [n,x,y]
        notas.sort()
    except ValueError:
        notas= "La entrada no es un entero."
    return notas

print(ordenar(n,x,y))