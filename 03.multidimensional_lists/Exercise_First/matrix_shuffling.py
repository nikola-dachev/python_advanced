rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    inner_list = [el for el in input().split()]
    matrix.append(inner_list)

while True:
    command = input()

    if command == 'END':
        break

    current_command = command.split()
    action = current_command[0]
    indexes = [el for el in (current_command[1:])]

    valid_rows = range(rows)
    valid_cols = range(cols)

    if action == 'swap' and len(indexes) == 4 and int(indexes[0]) in valid_rows and int(
            indexes[2]) in valid_rows and int(indexes[1]) in valid_cols and int(indexes[3]) in valid_cols:

        indexes = [int(el) for el in indexes]
        row_1, col_1, row_2, col_2 = indexes
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        for row in matrix:
            print(*row)

    else:
        print('Invalid input!')