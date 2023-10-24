"""Lea una secuencia creciente de números enteros (finaliza cuando se introduce un número
menor que el anterior) y muestre cuál es la media de los números introducidos. Si no se introdujeron al
menos dos términos válidos en la secuencia se debe mostrar “Secuencia no válida”. Por ejemplo, si la
secuencia leída es 1 3 67 800 901 900, se mostrará “ La media es 354.4, y la secuencia está formada por 5
números”. Si la secuencia leída es 10 9, el resultado es “Secuencia no válida”"""


def suma():
    cont=1
    n0= int(input("Dime un número: "))
    n1= int(input("Dime un número: "))
    comp= n0
    media=-1
    while n1>n0:
        comp +=n1
        cont +=1
        n0=n1
        n1= int(input("Dime un número: "))
    if cont != 1:
        media= comp/cont
        valida = True
    else:
        valida = False
    
    return valida, media, cont

valida, media, cont = suma()

if valida:
    print(f"la media es {media}, y hay {cont} números")
else:
    print('Secuencia no válida')
                        
                                            



        
        
