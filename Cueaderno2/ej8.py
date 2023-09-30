
x1= float(input("Valor de la x del primer punto?\n")) 
y1= float(input("Valor de la y del primer punto?\n"))
z1= float(input("Valor de la z del primer punto?\n"))

x2= float(input("Valor de la x del segundo punto?\n")) 
y2= float(input("Valor de la y del segundo punto?\n"))
z2= float(input("Valor de la z del segundo punto?\n"))

punto1 = [x1,y1,z1]
punto2 = [x2,y2,z2]

import math

def f(punto1:list,punto2:list):  #en el formato que se muestra arriba
    return( math.sqrt((punto1[0]-punto2[0])**2+(punto1[1]-punto2[1])**2+(punto1[2]-punto2[2])**2))
print(f(punto1,punto2))