"""Escribir un codigo para jugar a las damas. El tablero es una matriz de 8x8"""


def crear_tablero():
    """Crea un tablero de damas"""
    tablero = []
    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(' ')
        tablero.append(fila)
    return tablero


def imprimir_tablero(tablero):
    """Imprime el tablero de damas"""
    print('  0 1 2 3 4 5 6 7')
    print('  ---------------')
    for i in range(8):
        print(i, end='|')
        for j in range(8):
            print(tablero[i][j], end='|')
        print()
        print('  ---------------')
    
"""probar que imprima el tablero
tablero = crear_tablero()
imprimir_tablero(tablero)"""

def colocar_fichas(tablero):
    """Coloca las fichas en el tablero"""
    for i in range(8):
        for j in range(8):
            if i < 3 and (i+j)%2 != 0:
                tablero[i][j] = 'o'
            if i > 4 and (i+j)%2 != 0:
                tablero[i][j] = 'x'
    return tablero

"""probar que coloque las fichas
tablero = crear_tablero()
tablero = colocar_fichas(tablero)
imprimir_tablero(tablero)
"""

def mover_ficha(tablero, fila, columna, fila_nueva, columna_nueva):
    """Mueve una ficha en el tablero"""
    # Check if the move is a capture
    if abs(fila_nueva - fila) == 2 and abs(columna_nueva - columna) == 2:
        # Check if the captured square contains an opponent's piece
        if tablero[(fila + fila_nueva) // 2][(columna + columna_nueva) // 2] != ' ':
            # Remove the captured piece
            tablero[(fila + fila_nueva) // 2][(columna + columna_nueva) // 2] = ' '
            # Move the current piece
            tablero[fila_nueva][columna_nueva] = tablero[fila][columna]
            tablero[fila][columna] = ' '
            # Check for additional captures
            for dx, dy in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                if 0 <= fila_nueva + dx < 8 and 0 <= columna_nueva + dy < 8:
                    if tablero[fila_nueva + dx // 2][columna_nueva + dy // 2] != ' ' and \
                       tablero[fila_nueva + dx][columna_nueva + dy] == ' ':
                        mover_ficha(tablero, fila_nueva, columna_nueva, fila_nueva + dx, columna_nueva + dy)
    else:
        # Regular move
        tablero[fila_nueva][columna_nueva] = tablero[fila][columna]
        tablero[fila][columna] = ' '

    if fila_nueva == 0 and tablero[fila_nueva][columna_nueva] == 'o':
        # Change the piece to a queen
        tablero[fila_nueva][columna_nueva] = 'O'
    elif fila_nueva == 7 and tablero[fila_nueva][columna_nueva] == 'x':
        # Change the piece to a queen
        tablero[fila_nueva][columna_nueva] = 'X'

    return tablero
def mover_reina(tablero, fila, columna, fila_nueva, columna_nueva):
    """Mueve una reina en el tablero"""
    # Check if the move is a capture
    if abs(fila_nueva - fila) == abs(columna_nueva - columna):
        # Check if the path is clear (no pieces in the way)
        path_is_clear = True
        for i in range(1, abs(fila_nueva - fila)):
            if tablero[fila + i * ((fila_nueva - fila) // abs(fila_nueva - fila))][columna + i * ((columna_nueva - columna) // abs(columna_nueva - columna))] != ' ':
                path_is_clear = False
                break
        if path_is_clear:
            # Move the queen
            tablero[fila_nueva][columna_nueva] = tablero[fila][columna]
            tablero[fila][columna] = ' '
        else:
            print("Invalid move. Path is not clear.")
    else:
        print("Invalid move. Queens can only move diagonally.")
    return tablero
#probar que mueva la ficha
"""tablero = crear_tablero()
tablero = colocar_fichas(tablero)
imprimir_tablero(tablero)
tablero = mover_ficha(tablero, 2, 1, 3, 2)  
imprimir_tablero(tablero)
"""
def hay_movimientos_validos(tablero, jugador):
    """Check if there are any valid moves for the current player"""
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna].lower() == jugador:
                # Check if this piece has any valid moves
                for fila_dest in range(len(tablero)):
                    for columna_dest in range(len(tablero[fila_dest])):
                        if es_movimiento_valido(tablero, fila, columna, fila_dest, columna_dest):
                            return True
    return False

def obtener_movimiento_jugador():
    """Ask the player for a piece to move and a destination square"""
    fila = int(input("Enter the row of the piece to move: "))
    columna = int(input("Enter the column of the piece to move: "))
    fila_nueva = int(input("Enter the row of the square to move to: "))
    columna_nueva = int(input("Enter the column of the square to move to: "))
    return fila, columna, fila_nueva, columna_nueva

def juego_terminado(tablero):
    """Check if the game is over"""
    # The game is over if one player has no pieces left. Adjust this as needed.
    return 'o' not in tablero or 'x' not in tablero

def es_movimiento_valido(tablero, fila, columna, fila_nueva, columna_nueva):
    """Check if a move is valid"""
    # Check if the destination square is empty
    if tablero[fila_nueva][columna_nueva] != ' ':
        return False

    # Check if the piece is moving diagonally
    if abs(fila_nueva - fila) != abs(columna_nueva - columna):
        return False

    # Check if the piece is moving forward (for normal pieces)
    if tablero[fila][columna] in ['o', 'x'] and (fila_nueva - fila) != (-1 if tablero[fila][columna] == 'o' else 1):
        return False

    # Check if the piece is jumping over an opponent's piece
    if abs(fila_nueva - fila) == 2:
        if tablero[(fila + fila_nueva) // 2][(columna + columna_nueva) // 2] not in ['o', 'x', ' ']:
            return False

    return True

def main():
    # Create the board and place the pieces
    tablero = crear_tablero()
    tablero = colocar_fichas(tablero)

    # Main game loop
    while True:
        # Print the board
        imprimir_tablero(tablero)

        # Get the player's move
        fila, columna, fila_nueva, columna_nueva = obtener_movimiento_jugador()

        # Move the piece
        if tablero[fila][columna] in ['O', 'X']:
            tablero = mover_reina(tablero, fila, columna, fila_nueva, columna_nueva)
        else:
            tablero = mover_ficha(tablero, fila, columna, fila_nueva, columna_nueva)

        # Check if the game is over or if the current player has no valid moves
        if juego_terminado(tablero) or not hay_movimientos_validos(tablero, 'o' if tablero[fila][columna] == 'o' else 'x'):
            break

# Run the game
if __name__ == "__main__":
    main()



