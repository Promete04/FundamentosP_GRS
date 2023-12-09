
board = [[{} for _ in range(8)] for _ in range(8)]
board[0][0] = {'piece': 'pawn', 'color': 'black'}
board[6][3] = {'piece': 'pawn', 'color': 'white'} 

for row in board:
    print(row)

def move_pawn(board, current_position, new_position):
    x1, y1 = current_position
    x2, y2 = new_position
    mensaje= ""
    if not board[x2][y2]:
        board[x2][y2], board[x1][y1] = board[x1][y1], board[x2][y2]
        mensaje= "movimiento exitoso"
    else:
        mensaje= "no se puede mover ahi"
    return mensaje

print(move_pawn(board, (0,0), (1,0)))
print(move_pawn(board, (6,3), (5,3)))
for row in board:
    print(row)



    





    


