SIZE = 5
field = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

targets_on_the_field = 0
targets_hit = 0
position_of_the_hit_targets = []
position_of_the_hit_targets_inner_list = []
my_position = []

for _ in range(SIZE):
    inner_list = [el for el in input().split()]
    field.append(inner_list)

for row_index in range(SIZE):
    for col_index in range(SIZE):
        if field[row_index][col_index] == 'A':
            my_position = [row_index, col_index]

        if field[row_index][col_index] == 'x':
            targets_on_the_field += 1

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == 'move':
        new_row = my_position[0] + directions[direction][0] * int(command[2])  # command[2] are the steps
        new_col = my_position[1] + directions[direction][1] * int(command[2])

        if not (0 <= new_row < len(field) and 0 <= new_col < len(field)):
            continue
        if field[new_row][new_col] == 'x':
            continue

        my_position = [new_row, new_col]

    elif action == 'shoot':
        new_row = my_position[0] + directions[direction][0]
        new_col = my_position[1] + directions[direction][1]

        while 0 <= new_row < len(field) and 0 <= new_col < len(field):

            position_shot = False
            if field[new_row][new_col] == 'x':
                field[new_row][new_col] == '.'
                position_of_the_hit_targets_inner_list = [new_row, new_col]
                position_of_the_hit_targets.append(position_of_the_hit_targets_inner_list)
                targets_hit += 1
                position_shot = True
            new_row += directions[direction][0]
            new_col += directions[direction][1]
            if position_shot == True:
                break

        if targets_hit == targets_on_the_field:
            print(f"Training completed! All {targets_hit} targets hit.")
            break

if targets_hit < targets_on_the_field:
    print(f"Training not completed! {targets_on_the_field - targets_hit} targets left.")

print(*position_of_the_hit_targets, sep='\n')






