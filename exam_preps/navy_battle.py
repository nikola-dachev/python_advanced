rows = int(input())

matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

submarine_position = ()
mine_hits = 0
battle_cruisers = 3

for row in range(rows):
    inner_list = list(input())

    if 'S' in inner_list:
        submarine_position = (row, inner_list.index('S'))
    matrix.append(inner_list)
matrix[submarine_position[0]][submarine_position[1]] = '-'

while True:

    direction = input()

    new_row = submarine_position[0] + directions[direction][0]
    new_col = submarine_position[1] + directions[direction][1]

    if matrix[new_row][new_col] == '*':
        matrix[new_row][new_col] = '-'
        mine_hits += 1
        if mine_hits > 2:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
            matrix[new_row][new_col] = 'S'
            break

    elif matrix[new_row][new_col] == 'C':
        matrix[new_row][new_col] = '-'
        battle_cruisers -= 1
        if battle_cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            matrix[new_row][new_col] = 'S'
            break

    submarine_position = (new_row, new_col)

for row in matrix:
    print(*row, sep='')

