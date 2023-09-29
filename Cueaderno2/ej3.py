m= int(input("Numero de periodos?\n"))

tna= float(input("TNA?\n"))

def TIEA(tna:float,m:int):
    return((1+tna/m)**(m-1))
print(TIEA(tna,m))