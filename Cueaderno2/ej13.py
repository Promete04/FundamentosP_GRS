""". Haz un subprograma que determine los días, horas, minutos y segundos que
hay en una cantidad de segundos introducida por el usuario (desprecia las
fracciones de segundo). Escribe un probador para el mismo."""

import math

def f(segundos:int):
      #calculas los dias con decimales para arrastralos y los de verdad
  d1=(segundos/86400)    
  d2=(segundos//86400)
      #obtienes las horas de los decimales de los días
  h1=(d1-math.trunc(d1))*24
  h2= h1 - (h1 -  math.trunc(h1))
      #obtienes los minutos de los decimales de las horas
  m1=((h1-math.trunc(h1))*60)
  m2= m1 - (m1 -  math.trunc(m1))
      #lo mismo pero con los segundos de los minutos
  s = round((m1-math.trunc(m1))*60) 
  return d2, h2, m2, s

def probador():
    segundos = int(input("Segundos a convertir?\n"))
    d2, h2, m2, s = f(segundos)

    print(f"Días: {d2}")
    print(f"Horas: {h2}")
    print(f"Minutos: {m2}")
    print(f"Segundos: {s}")

probador()