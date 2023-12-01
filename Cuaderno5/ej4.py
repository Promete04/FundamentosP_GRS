"""Implementa una estructura que de soporte a los puntos en 2D, es decir, con dos
coordenadas x e y. Programa después funciones para su suma y resta.
"""

puntos= {}

def storage(puntos:dict,x:bool,y:bool,num:int)->dict:
    datos= (x, y)
    punto={num:datos}
    puntos.update(puntos)

def introduce_punto(puntos:dict)->str:
    num= int(input("Cuantos puntos quieres introducir? "))
    for i in range(num):
        x= input("Valor de x? ")
        y= input("Valor de y? ")
        storage(puntos, x, y, num)

puntos, x, y, num= introduce_punto(puntos)
storage(puntos, x, y, num)
"""
def suma(puntos:dict):
    x= input("que punto quieres sumar? ")
    y= input("con que punto quieres sumarlo? ")
    resultado= puntos.get(x) + puntos.get(y)
    return resultado

def resta(puntos:dict):
    x= input("que punto quieres restar? ")
    y= input("con que punto quieres restarlo? ")
    resultado= puntos.get(x) - puntos.get(y)
    return resultado

print(suma(puntos))
print(resta(puntos))
"""