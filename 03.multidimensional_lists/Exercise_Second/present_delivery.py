number_of_presents = int(input())
size = int(input())

nice_kids_visited = 0
nice_kids = 0
santa_position = []
neighbourhood_matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    neighbourhood_matrix.append(line)
    if 'S' in line:
        santa_position = [row, line.index('S')]
        neighbourhood_matrix[santa_position[0]][santa_position[1]] = '-'
    if 'V' in line:
        nice_kids += line.count('V')

while True:
    command = input()
    if command == 'Christmas morning':
        break

    santa_position = [
        santa_position[0] + directions[command][0],
        santa_position[1] + directions[command][1]
    ]

    house = neighbourhood_matrix[santa_position[0]][santa_position[1]]
    if house == 'V':
        nice_kids_visited += 1
        number_of_presents -= 1

    if house == 'C':
        for coordinates in directions.values():
            r = santa_position[0] + coordinates[0]
            c = santa_position[1] + coordinates[1]

            if neighbourhood_matrix[r][c].isalpha():
                if neighbourhood_matrix[r][c] == 'V':
                    nice_kids_visited += 1

                neighbourhood_matrix[r][c] = '-'
                number_of_presents -= 1

    neighbourhood_matrix[santa_position[0]][santa_position[1]] = '-'
    if not number_of_presents or nice_kids == nice_kids_visited:
        break

neighbourhood_matrix[santa_position[0]][santa_position[1]] = 'S'

if not number_of_presents and nice_kids_visited < nice_kids:
    print("Santa ran out of presents!")

print(*[' '.join(line) for line in neighbourhood_matrix], sep='\n')

if nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids - nice_kids_visited} nice kid/s.")


