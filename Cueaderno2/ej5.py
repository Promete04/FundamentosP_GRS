x= input("Valor de la x?\n")  #la pongo para dar el paripé, no vale para nada
y= float(input("Valor de la y?\n"))

def f(y):
    if (y>31.623): return("Está sobre la circunferencia")
    else: return ("No supera la circunferencia")
print(f(y))