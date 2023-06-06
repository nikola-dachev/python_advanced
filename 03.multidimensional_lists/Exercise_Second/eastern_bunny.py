size = int(input())

matrix = []
bunny_position = []
best_direction = None
best_path = []
max_eggs_collected = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if 'B' in line:
        bunny_position = [row, line.index('B')]

for direction, positions in directions.items():
    new_row = bunny_position[0] + positions[0]
    new_col = bunny_position[1] + positions[1]

    current_path = []
    collected_eggs = 0

    while 0 <= new_row < size and 0 <= new_col < size:
        if matrix[new_row][new_col] == 'X':
            break
        collected_eggs += int(matrix[new_row][new_col])
        current_path.append([new_row, new_col])

        new_row += positions[0]
        new_col += positions[1]
    if collected_eggs >= max_eggs_collected:
        max_eggs_collected = collected_eggs
        best_path = current_path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(f'{max_eggs_collected}')


