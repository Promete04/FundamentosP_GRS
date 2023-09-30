"""Implementa una función "fuerza" que retorne el valor de la magnitud física
fuerza a partir de los valores de masa y aceleración recibidos como
parámetros. Construye después un programa probador especificando los
casos de prueba necesarios que muestre por pantalla el valor de la fuerza a
partir de una masa y aceleración dadas.
"""
m=float(input("Masa el objeto?\n"))
a=float(input("Aceleración que experimenta\n"))
def f(m:float,a:float):
    return(m*a)
print(f(m,a))


