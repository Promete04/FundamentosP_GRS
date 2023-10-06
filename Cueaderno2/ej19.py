"""Python permite dar valores por defecto en la definición de un subprograma.
Documéntate y estudia cómo se hace esto. Para ello, ten en cuenta que la
presión es mucho más estable que la temperatura. Nota: Este ejercicio
pretende mostrarte que con la implementación de valores por defecto ya no
te harían falta los dos ejercicios anteriores. """


def vol(n:float,r=0.082, t=273.15):
    return (n*r*t)

print (f"{vol(5)} litros")