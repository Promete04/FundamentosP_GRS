import random

jugadores=[]
jugador1={}
jugador2={}
def establecer_jugadores():
    print("\nIngresen sus nombres, deben tener una longitud de entre 6 y 12 digitos.")
    while True:
        name_jugador1=input("Jugador 1, ingrese un nombre: ")
        if len(name_jugador1)<6 or len(name_jugador1)>12:
            print (f"Nombre {name_jugador1} no valido.")
        
        else:
            jugadores.append(name_jugador1)
            jugador1.update({"Nombre": f"{name_jugador1}"})
            print(f"{name_jugador1} ha sido añadido.")
            break
    while True:
        name_jugador2=input("Jugador 2, ingrese un nombre: ")
        if len(name_jugador2)<6 or len(name_jugador2)>12:
            print(f"Nombre {name_jugador2} no válido.")
        else:
            jugadores.append(name_jugador2)
            jugador2.update({"Nombre": f"{name_jugador2}"})
            print(f"{name_jugador2} ha sido añadido.")
            break
    return jugadores
    
        

orden=[]
def orden_jugadores(): 
    first=random.choice(jugadores)
    print(f"Le toca empezar a {first}")
    if first==jugadores[0]:
        sec=jugadores[1]
        orden.append(first)
        orden.append(sec)
    else:
        sec=jugadores[0]
        orden.append(first)
        orden.append(sec)
    first=orden[0]
    sec=orden[1]
    return orden

fichas=[]
def asignar_fichas():   #solo selecciona u njugador y se podría hacer aleatorio
    while True:
        ficha1=input(f"{orden[0]}, escriba una letra para la ficha (b o w): ")
        if len(ficha1)>1:
            return "No es válido."
        break
    if ficha1=="":
        ficha1={"Pieza1":"W"}  #FICHA BLANCA = W

    if orden[0]==jugadores[0]:
        jugador1.update({"Ficha":f"{ficha1}"})
    elif orden[0]==jugadores[1]:
        jugador2.update({"Ficha": f"{ficha1}"})
    
    while True:
        ficha2=input(f"{orden[1]}, escribe una letra para las fichas: ")
        if len(ficha2)>1:
            return "No es válido."
        break
    if ficha2=="":
        ficha2={"Pieza2":"B"}   #FICHA NEGRA = B
    if orden[1]==jugadores[0]:
        jugador1.update({"Ficha":f"{ficha2}"})
    elif orden[1]==jugadores[1]:
        jugador2.update({"Ficha": f"{ficha2}"})
    fichas.append(ficha1)
    fichas.append(ficha2)
    return fichas


def crear_tablero():
    tablero = []
    for i in range(8):
        fila = []
        for j in range(8):
            if (i + j) % 2 == 0:
                if i < 3:
                    fila.append(fichas[0])  # Ficha negra
                elif i > 4:
                    fila.append(fichas[1])  # Ficha blanca
                else:
                    fila.append(" ")  # Espacio vacío
            else:
                fila.append(" ")  # Espacio vacío
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    print("  A B C D E F G H ")
    for i in range(8):
        fila_str = str(i+1) + "|"
        for j in range(8):
            fila_str += tablero[i][j] + "|"
        print(fila_str)
    print("-----------------")

# Ejemplo de uso, tengo que establecer la funcion principal.
jugadores=establecer_jugadores()
print(jugadores)
orden_jugadores()
fichas=asignar_fichas()
tablero = crear_tablero()
imprimir_tablero(tablero)
