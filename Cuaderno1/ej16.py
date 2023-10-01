""". Haz un programa que pida al usuario dos textos (cadenas de caracteres) y
los muestre en pantalla en orden alfabético. Pruébalo también introduciendo
cadenas de caracteres que sean numéricas, por ejemplo 99 y 102 y razona
sobre la salida producida"""

cad=input("Intruduce caracteres (sin comas de por medio):") 
ordenado = sorted(cad)

print(ordenado)