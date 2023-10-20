"""x=input("Dime un ángulo\n")
y=input("Dime otro ángulo\n")
z=input("Dime el último  ángulo\n")"""

def angulos(x:float,y:float,z:float)-> str:
    type = None
    try:
        x= float(x)
        y= float(y)
        z= float(z)
        if x+y+z  == 180:
            if z == x == y: 
                type = "Rectángulo"
            elif x==y or x==z or y==z:
                type= "Acutángulo"
            else:
                type= "Obtusángulo"
        else:     
             type= "Los ángulos no suman 180º"
    except ValueError:
        type = "Input incorrecto"
    return type

def ternas_aleatorias():
    import random
    x=0
    y=0
    z=0
    while  (x+y+z !=180):
        x= random.randint(0,180+1)
        y=random.randint(0,180+1)
        z=random.randint(0,180+1)
    return x, y ,z

x,y,z = ternas_aleatorias()


print(x,y,z)
print(angulos(x,y,z))