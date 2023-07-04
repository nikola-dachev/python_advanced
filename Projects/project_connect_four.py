from collections import deque
from colorama import Fore

def place_circle():
    row = 0
    while row != ROWS and matrix[row][player_col] == '0':
        row +=1
    matrix[row -1][player_col] = player_symbol

    return row -1

def check_for_win(row, col):
    for x, y in directions:
        count = 1
        for i in range(1,4):
            new_row = row + x * i
            new_col = col + y * i

            if not (0<= new_row < ROWS and 0<= new_col <COLS):
                break
            if matrix[new_row][new_col] !=player_symbol:
                break

            count +=1


        for i in range(1,4):
            new_row = row - x * i
            new_col = col - y * i

            if not (0<= new_row < ROWS and 0<= new_col <COLS):
                break
            if matrix[new_row][new_col] !=player_symbol:
                break

            count +=1

        if count >=4:
            return True

    if counter_for_draw == ROWS * COLS:
        print('DRAW')
        [print(f"[ {', '.join(row)} ]") for row in matrix]
        raise SystemExit

    return False

ROWS = 6
COLS = 7
counter_for_draw = 0

matrix = [["0"] * COLS for row in range(ROWS)]

player_one_symbol = Fore.GREEN + "1" + Fore.RESET
player_two_symbol = Fore.BLUE + "2" + Fore.RESET

turns = deque([[1,player_one_symbol],[2,player_two_symbol]])

win = False

directions = {
    (0,1), #right
    (0,-1), # left
    (1,0), #down
    (-1,0), #up
    (-1,-1), #top left
    (-1,1), # top right
    (1,-1), # bottom left
    (1,1) #bottom right
}

while not win:
    [print(f"[ {', '.join(row)} ]") for row in matrix]

    player_number, player_symbol = turns[0]

    try:
        player_col = int(input(f"Player {player_number} choose a column: ")) - 1

    except ValueError:
        print(Fore.RED + f"Please choose a valid number in range(1 - {COLS})" + Fore.RESET)
        continue

    if not 0 <= player_col < COLS:
        print(Fore.RED + f"Please choose a valid number in range(1 - {COLS})" + Fore.RESET)
        continue

    if matrix[0][player_col] != "0":
        print(Fore.RED + "No empty space on that column , choose another one"+ Fore.RESET)
        continue

    row = place_circle()
    counter_for_draw +=1
    win = check_for_win(row, player_col)

    turns.rotate()

print(f'Player{turns[1][0]} wins')
matrix = [["0"] * COLS for row in range(ROWS)]
