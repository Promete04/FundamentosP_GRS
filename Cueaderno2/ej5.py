"""Escribe una función que determine si un punto de coordenadas en 2D está o
no sobre la circunferencia x2+y2=1000.
"""

x= input("Valor de la x?\n")  #la pongo para dar el paripé, no vale para nada
y= float(input("Valor de la y?\n"))

def f(y):
    if (y>31.623): return("Está sobre la circunferencia") #31.623 es el punto más alto de la circunferencia
    else: return ("No supera la circunferencia")
print(f(y))