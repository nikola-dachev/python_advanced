rows, cols = [int(el) for el in input().split(',')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
mouse_position = ()
number_of_cheese = 0

for row in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

    if 'M' in inner_list:
        mouse_position = (row, inner_list.index('M'))
        matrix[mouse_position[0]][mouse_position[1]] = '*'

    if 'C' in inner_list:
        number_of_cheese += inner_list.count('C')

while True:
    direction = input()

    if direction == 'danger':
        print("Mouse will come back later!")
        matrix[new_row][new_col] = 'M'
        break

    new_row = mouse_position[0] + directions[direction][0]
    new_col = mouse_position[1] + directions[direction][1]

    if not (new_row < rows and new_col < cols):
        matrix[mouse_position[0]][mouse_position[1]] = 'M'
        print("No more cheese for tonight!")
        break

    if matrix[new_row][new_col] == 'C':
        number_of_cheese -= 1
        matrix[new_row][new_col] = '*'
        if number_of_cheese == 0:
            matrix[new_row][new_col] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[new_row][new_col] == 'T':

        matrix[new_row][new_col] = 'M'
        print("Mouse is trapped!")
        break

    elif matrix[new_row][new_col] == '@':
        new_row = mouse_position[0]
        new_col = mouse_position[1]
        continue

    mouse_position = (new_row, new_col)

for row in matrix:
    print(*row, sep='')
