rows, cols = [int(el) for el in input().split()]

matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_position = ()
number_of_moves = 0
touched_opponents = 0

for row in range(rows):
    inner_list = input().split()
    matrix.append(inner_list)

    if 'B' in inner_list:
        player_position = (row, inner_list.index('B'))
        matrix[player_position[0]][player_position[1]] = '-'

while True:
    direction = input()

    if direction == 'Finish':
        break

    if touched_opponents == 3:
        break

    new_row = player_position[0] + directions[direction][0]
    new_col = player_position[1] + directions[direction][1]

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        new_row = player_position[0]
        new_col = player_position[1]

    elif matrix[new_row][new_col] == 'O':
        new_row = player_position[0]
        new_col = player_position[1]


    elif matrix[new_row][new_col] == '-':
        number_of_moves += 1

    elif matrix[new_row][new_col] == 'P':
        touched_opponents += 1
        number_of_moves += 1
        matrix[new_row][new_col] = '-'

    player_position = (new_row, new_col)

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {number_of_moves}")



