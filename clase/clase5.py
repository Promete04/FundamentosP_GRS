"""
def inverso(x:float):
    #X!=0
    i=1/x
    return i

for i in range (1,10):
    print (i)


for i in range(1,10):
    for j in range (1,i):
        print ("*",end=" ")
    print()

    """
def funcion (x) :
    """int —> int
    OBJ: Este codigo no fue documentado"""
    a = 0
    while ((not x) ==  0):
        a += x%10
        x //= 10
    return a
print (funcion (60))


def dibujarRombo (filas:int):
    for i in range (1,filas+1):
        for j in range (i,filas):
            print (" ",end = " ")
        for j in range (i,filas+i):
            print("*", end= " ")
        print()
    return

dibujarRombo(6)