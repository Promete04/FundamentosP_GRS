"""continuacion de clase de diccionarios"""

def contar_letras(texto):
    d={}
    for c in texto.replace(" ",""):
        d[c.upper()] = d.get(c.upper(),0) + 1
    return d

t1= "William Shakespeare"
t2= "I a weakish speaker"
d1= contar_letras(t1)
d2= contar_letras(t2)
print(d1)
print(d2)

"""Si tengo que buscar una cosa de las dos y
 sacar la otra en el for utilizar dos variables for key,iten in dic.items"""

def dnd_mas_personitas(dict):
    d={}
    max_value= 0 
    max_key= None
    for key, value in dict.items():
        d[value] = d.get[value,0]
        if d[value] > max_value:
            max_value = d[value]
            max_key = key
    return max_key


def to_dict(products:list,prices:list,discounts:list):
    d={}
    for  products, prices, discounts in zip(products,prices,discounts):
        d[products]={"price":prices,"discount":discounts}
    return d

def imprimir_antes(n):
    if n > 0:
        print(n)
        imprimir_antes(n - 1)

def imprimir_despues(n):
    if n > 0:
        imprimir_despues(n - 1)
        print(n)

n=10
imprimir_antes(n)
imprimir_despues(n)
