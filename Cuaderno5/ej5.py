import ej4
import math
puntos= ej4.puntos

def dist(puntos:dict):
    x, y= input("que punto quieres medir? "), input("con que punto quieres medirlo? ")
    d = math.sqrt((puntos.get(x[0])-puntos.get(y[0]))**2+(puntos.get(x[1])-puntos.het(y[1]))**2)
    return d

print(dist(puntos))