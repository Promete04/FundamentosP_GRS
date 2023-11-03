def leer_numero ():
    end= False
    valid=False
    while not valid and not end:
        try:
            n= input("Dime un numero o FIN\t ")
            if n == "FIN":
                end = True
                valid= True
                n= None
            else:
                n = int(n)
                valid= True
        except ValueError:
            valid = False
    return n, end

leer_numero()
