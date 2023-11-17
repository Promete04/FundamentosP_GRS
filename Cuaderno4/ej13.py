"""Realizar un programa que lea palabras hasta que se introduzca “fin”, mostrando
un recuento de las longitudes de las palabras, es decir, el número total de
palabras de longitud 1 que se hayan introducido, el total de longitud 2, etc. La
máxima longitud de las palabras deberá ser de 15 caracteres. Una posible salida
de este programa sería:
Palabras longitud 1: ninguna
Palabras longitud 2: 10
…
Palabras longitud 15: 1"""

def num_palabras(texto:str)->str:
    texto= texto.split()
    lista=[]
    for palabra in texto:
        if palabra == "FIN":
            break #lo pongo pq si no me muero
        if len(palabra) <= 15:
            lista.append(len(palabra))
        else:
            print("La palabra",palabra,"es demasiado larga")
    for i in range(1,16):
        if i in lista:
            print("Palabras longitud",i,":",lista.count(i))
        else:
            print("Palabras longitud",i,": ninguna")
    return None

texto= "hola que tal estas FIN"
print(num_palabras(texto))

