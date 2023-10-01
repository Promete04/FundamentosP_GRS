"""Siguiendo con lo anterior, implementa ahora un subprograma que calcule el
volumen de un gas en condiciones ideales. ¡No olvides reutilizar tu esfuerzo
no reescribiendo código que ya tienes de ejercicios anteriores, sino
invocándolo! Por cierto, que tu nuevo subprograma debería tener tan solo una
línea de código, tenlo en cuenta. Y no olvides probarlo.
𝑉 = nRT/P
"""
n= float(input("Moles del gas?\n"))

def f(n:float):
    return(n*0.082*273.15)

print(str(f(n))+" litros")

