def suma():
    acc=0
    n=0
    cont=0
    while n != "FIN":
        try:
            n= float(input("Dime un número o FIN?\n"))
            acc= acc+n
            cont +=1
            x= round(acc)
        except ValueError:
            return "Error"
    return x, cont
print(suma())
        
        
