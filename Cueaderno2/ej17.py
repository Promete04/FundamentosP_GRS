"""Se dice que un gas está en condiciones ideales cuando está a 1 atmosfera de
presión y 0ºC, es decir 273,15ºK. Escribe una función que determine si un
cierto gas se encuentra en condiciones ideales.
𝑉 = nRT/P
"""

#n= float(input("Moles de gas?\n"))    los pongo en comentario para que funcione el ej18

def vol(n:float):
    r = 0.082
    t = 273.15
    v_out = r*n*t
    return (v_out)

# v= float(input("Volumen del gas? (en litros)\n"))

print(v==vol(n))

