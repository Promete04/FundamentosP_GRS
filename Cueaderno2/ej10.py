""". Una aplicación leerá de teclado los valores necesarios para mostrar en
pantalla el área de un círculo, un cuadrado y un triángulo. No queremos
implementar la aplicación completa aún, sólo preparar los subprogramas de
que necesitaremos disponer para en un futuro construir la aplicación
(funciones que leen de teclado números y los validan, por una parte, y
funciones que hacen los cálculos de las distintas áreas, por otra). Nota: si lo
necesitas, utiliza como aproximación de П (pi) el valor de que proporciona la
biblioteca “math” de Python.
"""
import math
tipo = input("Que area quieres calcular? (círculo,cuadrado o triángulo)\n")

def datos(tipo:str,b,h,r):
    if tipo == "cuadrado" or "triángulo":
        return(float(b=input("Base del {tipo}?\n")))
        return(float(h=input("Altura del {tipo}?\n")))
        r=None
    else:
        return(float(r=input("Radio del {tipo}")))
        b=None
        h=None
    print(datos(tipo,b,h,r))       
        

def areas(tipo:str,b:float,r:float,h:float):
    if tipo == "triángulo": 
        return ((b*h)/2)
    else:
        if tipo == "círculo":
            return (math.pi*(r**2))
        else:
            return (b*h)
    print(str(areas(b,r,h))+" metros cuadrados")