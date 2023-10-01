""". La temperatura expresada en grados centígrados TC, se puede convertir a
grados Fahrenheit (TF) mediante la siguiente fórmula:
TF = 9.0*TC/5.0 + 32.0
Escribe un programa que utilizando un cierto valor de temperatura en grados
Fahrenheit, muestre en pantalla la temperatura equivalente en grados
Centígrados."""

temp_f = float(input("Temperatura en grados Fahrenheit\n"))  #pedrimos la temepratura en fahrenheit

temp_c = float((temp_f-32.0)*5.0/9.0)   #transformamos la temperatura a celsius

temp_c_red = round(temp_c,2)  #redondeamos la temperatura con dos decimales

print(f"{temp_f}ºF son {temp_c_red}ºC")