"""Escribe un código que pide al vendedor el importe de una compra: Si la compra es
superior a 100EUR se aplica un descuento del 5% si se paga al contado, pero si el
pago es con tarjeta sólo se aplica el 2%. Asegúrate de que el importe de la compra
es un número válido antes de proceder a los cálculos (pista: usa try para
comprobar que es posible convertir la entrada a un float)."""

import math

coste= input("Coste de la compra")
modo_pago= input("Modo de pago? (al contado, tarjeta)")
try:
    float(coste)
    def precio(coste:float):
        n=None
        if coste > 100: 
            if modo_pago== "al contado":
                n= (coste*(1-0.05))         
            else: 
                n= (coste)*(1-0.02)
        else:
            n= (coste)  
        return(n)      # programación estructurada
except TypeError:
    print ("Entrada no válida")
