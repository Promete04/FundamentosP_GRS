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

