"""La ley de los gases ideales indica que el volumen V (en litros) ocupado por n
moles de un gas a presión P (en atmósferas) y temperatura T (en grados
Kelvin), responde a la siguiente fórmula:
𝑉 = nRT/P
siendo R la constante universal de los gases cuyo valor es 0,082 atmósferas
litro/Kmol. Hagamos un subprograma que calcule el volumen de un gas a
partir de su presión y temperatura y probémoslo."""

p=float(input("Presión? (en atmósferas)\n"))
t=float(input("Temperatura? (en kelvin)\n"))
n=float(input("Moles de gas?\n"))
def v(p:float,t:float,n:float):
    r= 0.082
    return((n*r*t)/p)
print(str(v(p,t,n))+" litros")
    
