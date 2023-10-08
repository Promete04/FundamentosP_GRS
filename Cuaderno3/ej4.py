"""Reprograma lo hecho en el ejercicio 2 para reutilizar el validador de enteros del
ejercicio 3. Obviamente, tendrás que seguir validando que los valores de hora y
minutos se encuentran en el rango correcto."""


def validar_entero(input):
    try:
        int(input)  
        return True  
    except ValueError:
        return False  

def convertir_hora(hora_24):
    if ":" in hora_24:
        horas, minutos = hora_24.split(':')

        if validar_entero(horas) and validar_entero(minutos):
            horas, minutos = int(horas), int(minutos)

            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                if horas < 12:
                    periodo = "AM"
                    if horas == 0:
                        horas = 12  
                else:
                    periodo = "PM"
                    if horas > 12:
                        horas -= 12  

                hora_12 = f"{horas}:{minutos} {periodo}"
                return hora_12
            else:
                return "Hora fuera de rango"
        else:
            return "Entrada no válida"
    else:
        return "Formato incorrecto, debe ser hh:mm"
    
hora_24 = input("Ingrese una hora (hh:mm): ")
hora_12 = convertir_hora(hora_24)
print(hora_12)