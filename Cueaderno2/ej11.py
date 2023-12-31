"""El calendario gregoriano estableció (1582) que un año es bisiesto si es divisible
entre 4, a menos que sea divisible entre 100. Sin embargo, si un año es
divisible entre 100 y además es divisible entre 400, también resulta bisiesto.
Implementa una función que determine si un año es bisiesto o no y escribe
un probador para todos los posibles casos. Este probador debe mostrar en
pantalla, por ejemplo, si has puesto una variable anno= 2015, una salida
como la siguiente: "el año 2015 ¿es bisiesto?: False".
Resuelve los problemas poco a poco, prueba primero si es divisible por 4.
Cuando lo tengas ve añadiendo el resto de las condiciones.
Error frecuente: considerar que necesitas una instrucción if. Los booleanos se
pueden operar como el resto de los tipos.
"""

anno= int(input("Introduce un año para comprobar si es bisiesto\n"))

def bisiesto(anno):
    resultado = (" es bisiesto" if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0) else "no es bisiesto")
    return resultado

print(f"{anno} {bisiesto(anno)}")