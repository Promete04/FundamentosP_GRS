"""Escribe un subprograma que lea una hora en notación de 24 horas y la devuelva
en notación de 12 horas (ejemplo: las 18:30 serán las 6:30 PM). Pruébalo utilizando
valores introducidos por el usuario, pero no olvides validad las entradas para
asegurarte de que se trata de valores en el rango correcto"""

hora= input("Hora actual (en hh:mm): ")

horas= int(hora[0]+hora[1])
minutos=int(hora[3]+hora[4])

def cambio(horas:int, minutos:int):
    try:
         if 0 <= horas <= 23 and 0 <= minutos <= 59:
            if horas < 12:
                p = "AM"
                if horas == 0:
                    horas = 12  
            else:
                
                p = "PM"
                if horas > 12:
                    horas -= 12
            return str(horas) + ":" + str(minutos) + " " + p
         else:
            return "Hora fuera de rango"
    except ValueError:
        return "Entrada no válida"
    

print(cambio(horas,minutos))  