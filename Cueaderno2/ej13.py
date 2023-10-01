""". Haz un subprograma que determine los días, horas, minutos y segundos que
hay en una cantidad de segundos introducida por el usuario (desprecia las
fracciones de segundo). Escribe un probador para el mismo."""
import math
segundos=int(input("Segundos a convertir?\n"))

def f(segundos:int):
  d=(segundos/86400)    #calculas los dias
  h=((d-math.trunc(d))*24) #obtienes las horas de los decimales de los días
  m=((h-math.trunc(h))*60) #obtienes los minutos de los decimales de las horas
  s=round((m-math.trunc(m))*60) #lo mismo pero con los segundos de los minutos
  return(str(int(d-(d-math.trunc(d))))+" días", str(int(h-(h-math.trunc(h))))+" horas",  
         str(int(m-(m-math.trunc(m))))+" minutos", str(s)+" segundos")  #vas quitando los decimales de los datos y bajandolos en la cadena de tiempo d->h->m->s
print(f(segundos))   
