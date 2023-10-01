"""Se dice que un gas está en condiciones ideales cuando está a 1 atmosfera de
presión y 0ºC, es decir 273,15ºK. Escribe una función que determine si un
cierto gas se encuentra en condiciones ideales.
𝑉 = nRT/P
"""
v= float(input("Volumen del gas? (en litros)\n"))
n= float(input("Moles de gas?\n"))

def f(v:float,n:float):
    r= 0.082
    return (v/(n*r)==273.15)
print(f(v,n))