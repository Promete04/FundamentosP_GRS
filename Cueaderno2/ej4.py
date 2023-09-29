hora= input("Hora actual (en hh:mm:ss)\n")
horas= int(hora[0]+hora[1])
minutos=int(hora[3]+hora[4])
segundos=int(hora[6]+hora[7])

def f(horas:int,minutos:int,segundos:int):
    return((horas*3600+minutos*60+segundos))
print(str(f(horas,minutos,segundos))+" segundos desde la medianoche")
    


