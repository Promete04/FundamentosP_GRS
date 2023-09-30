""". Haz un subprograma que determine los días, horas, minutos y segundos que
hay en una cantidad de segundos introducida por el usuario (desprecia las
fracciones de segundo). Escribe un probador para el mismo."""
import math
segundos=int(input("Segundos a convertir?\n"))

def f(segundos:int):
  d=(segundos/86400)
  h=((d-math.trunc(d))*24)
  m=((h-math.trunc(h))*60)
  s=round((m-math.trunc(m))*60)
  return(str(int(d-(d-math.trunc(d))))+" días", str(int(h-(h-math.trunc(h))))+" horas",
         str(int(m-(m-math.trunc(m))))+" minutos", str(s)+" segundos")
print(f(segundos))
