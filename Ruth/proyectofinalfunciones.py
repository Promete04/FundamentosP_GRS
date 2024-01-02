import random
jugadores=[]  #lista para los nombres de los jugadores
jugador1={}   #diccionario con los datos del primer jugador añadido
jugador2={}   #diccionario con los datos del segundo jugador añadido
def establecer_jugadores():
    print("\nIngresen sus nombres, deben tener una longitud de entre 6 y 12 digitos.")
    while True:    #para devolver al mismo sitio en caso de que sea erroneo
        name_jugador1=input("Jugador 1, ingrese un nombre: ")
        if len(name_jugador1)<6 or len(name_jugador1)>12 or not name_jugador1.isalnum():
            print (f"Nombre {name_jugador1} no valido.")       
        else:
            jugadores.append(name_jugador1)
            jugador1.update({"Nombre": f"{name_jugador1}"})  #agregando el primer dato al diccionario del primer jugador
            print(f"{name_jugador1} ha sido añadido.")
            break
    while True:     #para devolver al mismo sitio en caso de que sea erroneo
        name_jugador2=input("Jugador 2, ingrese un nombre: ")
        if len(name_jugador2)<6 or len(name_jugador2)>12:
            print(f"Nombre {name_jugador2} no válido.")
        else:
            jugadores.append(name_jugador2)
            jugador2.update({"Nombre": f"{name_jugador2}"}) #primer dato del segundo jugador
            print(f"{name_jugador2} ha sido añadido.")
            break
    return jugadores

orden=[]
def orden_jugadores(): 
    first=random.choice(jugadores)  #eleccion aleatoria entre los jugadores de la lista de jugadores
    print(f"Le toca empezar a {first}")
    if first==jugadores[0]: #para poder establecer la información organizada en la lista de orden
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

tablero = []
def crear_tablero():
    for i in range(8): #accedo a cada fila del tablero
        fila = []
        for j in range(8): #accedo a cada elemento de cada fila
            if (i + j) % 2 == 0:
                if i < 3:
                    fila.append({"color": "B"})  # Ficha blanca, en un diccionario para que quede en diccionarios dentro del tablero
                    if orden[0]== jugador1['Nombre']:
                        jugador1.update({"color":"B"})
                    else:
                        jugador2.update({"color":"B"})
                elif i>4:
                    fila.append({"color": "N"})  # Ficha Negra
                    if orden[1]== jugador1['Nombre']:
                        jugador1.update({"color":"N"})
                    else:
                        jugador2.update({"color":"N"})
                else:
                    fila.append({"color":" "})
            else:
                fila.append({"color": " "})  # Espacio vacío
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    print("  A B C D E F G H")
    for i in range(8):
        coordnum= str(i+1) + "|"
        for j in range(8):
            coordnum+= f"{tablero[i][j]["color"]}" + "|"

        print(coordnum)
        
    print("-------------------------")
# A partir de aqui empieza el juego , empieza el programa de los movimientos

"""letras= {{"A": tablero[i][0] , "B": tablero[i][1], "C": tablero[i][2], "D":tablero[i][3], "E": tablero[i][4], "F": tablero[i][5], "G": tablero[i][6], "H": tablero[i][7]}for i in tablero}
"""

def actualizar_tablero(tablero, posicion_actual, posicion_nueva,situacion):
    x1, y1 = posicion_actual
    x2, y2 = posicion_nueva
    # Comprobar si es un movimiento de captura
    if abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
        tablero[(x1 + x2) // 2][(y1 + y2) // 2] = ' '
    tablero[x2][y2], tablero[x1][y1] = tablero[x1][y1], ' '
    # Comprobar que si esta en la linea de sucesión (debe ser reina?)
    if x2 == 0 and tablero[x2][y2] == 'N':
        tablero[x2][y2] = 'NQ'  # CORONACION DE LA REINA NEGRA
    elif x2 == 7 and tablero[x2][y2] == 'B':
        tablero[x2][y2] = 'BQ'  # CORONACION DE LA REINA BLANCA
    return tablero

def juego_acabado(tablero):
    fichas_blancas = 0
    fichas_negras = 0
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "B":
                fichas_blancas += 1
                if puede_moverse_blancas(tablero):
                    return False
            elif tablero[i][j] == "N":
                fichas_negras += 1
                if puede_moverse_negras(tablero):
                    return False
    if fichas_blancas == 0 or fichas_negras == 0:
        return True
    else:
        return False
    
def puede_moverse_blancas(tablero):
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "B":
                # Check all possible moves and captures for a white piece
                for dx, dy in [(-1, -1), (-1, 1)]:
                    if 0 <= i + dx < 8 and 0 <= j + dy < 8 and tablero[i + dx][j + dy] == ' ':
                        return True
                    if 0 <= i + 2*dx < 8 and 0 <= j + 2*dy < 8 and tablero[i + dx][j + dy] == 'N' and tablero[i + 2*dx][j + 2*dy] == ' ':
                        return True
    return False

def puede_moverse_negras(tablero):
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == "N":
                # Check all possible moves and captures for a black piece
                for dx, dy in [(1, -1), (1, 1)]:
                    if 0 <= i + dx < 8 and 0 <= j + dy < 8 and tablero[i + dx][j + dy] == ' ':
                        return True
                    if 0 <= i + 2*dx < 8 and 0 <= j + 2*dy < 8 and tablero[i + dx][j + dy] == 'B' and tablero[i + 2*dx][j + 2*dy] == ' ':
                        return True
    return False 


    

def movimiento_gen(tablero):
    posicion_actual=input("Escribe la posicion inicial(numero, letra en mayúscula): ")
    posicion_nueva=input("Escribe la posicion de destino: ")
    x1, y1 = posicion_actual
    x2, y2 = posicion_nueva
    if abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
        # It's a capture, call the appropriate function
        return capturar_pieza(tablero, posicion_actual, posicion_nueva,"comer")
    elif abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
        # It's a regular move, call the appropriate function
        return mover_pieza(tablero, posicion_actual, posicion_nueva,"comer")
    else:
        # It's an invalid move
        return "Movimiento inválido"

def mover_pieza(tablero, posicion_actual, posicion_nueva):
    x1, y1 = posicion_actual
    x2, y2 = posicion_nueva
    output=None
    #comprobar si moviemiento es valido para blancas
    if tablero[x1][y1] == "B":
        if not tablero[x2][y2]:
            output= actualizar_tablero(tablero, posicion_actual, posicion_nueva,"mover")
        else:
            output= "No se puede mover ahi, espacio ocupado"
            movimiento_gen(tablero)
    #comprobar si movimiento es valido para negras
    elif tablero[x1][y1] == "N":
        if not tablero[x2][y2]:
            output= actualizar_tablero(tablero, posicion_actual, posicion_nueva,"mover")
        else:
            output= "No se puede mover ahi, espacio ocupado"
            movimiento_gen(tablero)
    else:
        output= "No hay ninguna pieza en esa posicion"
        movimiento_gen(tablero)
    return output

def capturar_pieza(tablero, posicion_actual, posicion_nueva):
    x1, y1 = posicion_actual
    x2, y2 = posicion_nueva
    output=None
    #comprobar si movimiento es valido para blancas
    if tablero[x1][y1] == "B":
        if not tablero[x2,y2]:
            if tablero[x2-1][y2-1] == "N" or tablero[x2-1][y2+1] == "N": #comprobar si hay una ficha negra en diagonal 
                output= actualizar_tablero(tablero, posicion_actual, posicion_nueva)
        else:
            output= "No se puede mover ahi, espacio ocupado"
            movimiento_gen(tablero)
    #comprobar si movimiento es valido para negras
    elif tablero[x1][y1] == "N":
        if not tablero[x2,y2]:
            if tablero[x2+1][y2+1]=="B" or tablero[x2+1][y2-1]=="B": #comprobar si hay una ficha blanca en diagonal
                output= actualizar_tablero(tablero, posicion_actual, posicion_nueva)
        else:
            output= "No se puede mover ahi, espacio ocupado"
            movimiento_gen(tablero)
    else:
        output= "No hay ninguna pieza en esa posicion"
        movimiento_gen(tablero)
    return output

def main():
    jugadores = establecer_jugadores()
    print(jugadores)
    orden_jugadores()
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    print(jugador1)
    print(jugador2)

    while True:
        for jugador in jugadores:
            print(f"Le toca a {jugador}")
            movimiento_gen(tablero)
            imprimir_tablero(tablero)
            if juego_acabado(tablero):
                print("Juego acabado")
                break
            
            

if __name__ == "__main__":
    main()




    



