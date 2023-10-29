rows = int(input())

matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

my_position = ()
fish_catched = 0
is_caught_in_whirlpool = False

for row in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

    if 'S' in inner_list:
        my_position = (row, inner_list.index('S'))
        matrix[my_position[0]][my_position[1]] = '-'

while True:
    direction = input()

    if direction == 'collect the nets':
        break

    new_row = my_position[0] + directions[direction][0]
    new_col = my_position[1] + directions[direction][1]

    if not(0<= new_row):
        new_row = rows - 1

    if not(new_row < rows):
        new_row = 0

    if not(0<= new_col):
        new_col = rows - 1

    if not (new_col < rows):
        new_col = 0

    if matrix[new_row][new_col].isdigit():
        fish_catched += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = '-'

    elif matrix[new_row][new_col] == 'W':
        fish_catched = 0
        is_caught_in_whirlpool = True
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_row},{new_col}]")
        break

    my_position = (new_row, new_col)



if is_caught_in_whirlpool == False:
    if fish_catched >= 20:
        print("Success! You managed to reach the quota!")

    elif fish_catched < 20:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_catched} tons of fish more.")


    if fish_catched > 0:
        print(f"Amount of fish caught: {fish_catched} tons.")

    matrix[my_position[0]][my_position[1]] = 'S'
    for row in matrix:
        print(*row, sep = '')