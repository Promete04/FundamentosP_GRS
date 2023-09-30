"""La temperatura expresada en grados centígrados TC, se puede convertir a
grados Fahrenheit (TF) mediante la siguiente fórmula: TF = 9*TC/5 + 32.
Igualmente, es sabido que −273,15 °C corresponden con el 0 Kelvin. Escribe
una función devuelva la temperatura en grados Farenheit y otra en Kelvin a
partir de la temperatura en grados centígrados. Escribe un programa para
probarlas que a partir de una temperatura en grados centígrados obtenga e
imprima por pantalla la temperatura en Kelvin y Farenheit."""

ºc= float(input("Grados centígrados?\n"))

def k(ºc:float):
    return(ºc+273.15)


def f(ºc:float):
    return(9*(ºc/5)+32)


print(str(k (ºc))+" Kelvins")
print(str(f (ºc))+" grados Fahrenheit")