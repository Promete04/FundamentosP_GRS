"""Escribe un programa que dada una hora (expresada en hora, minutos y
segundos) muestre por pantalla el total de segundos transcurridos desde la
última medianoche y los que quedan para la siguiente medianoche."""

Hora_actual = [12, 50, 30]  #horas, minutos, segundos 


Segundos_actuales = Hora_actual[2]+Hora_actual[1]*60+Hora_actual[0]*3600
Segundos_dia = 24*3600

Tiempo1 = Segundos_dia-Segundos_actuales  #segundos hasta medianoche
Tiempo2 = Segundos_dia-Tiempo1 #segundo desde la medianoche

print(f"Tiempo desde la medianoche: {Tiempo1} segundos \nTiempo hasta la medianoche: {Tiempo2} segundos")