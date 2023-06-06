size =  int(input())

matrix = []
collected_tea_bags = 0
alice_position = []

directions = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0,1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if 'A' in line:
        alice_position = [row,line.index('A')]
        matrix[alice_position[0]][alice_position[1]] = '*'

while collected_tea_bags < 10:
    command = input()

    new_row = alice_position[0]+ directions[command][0]
    new_col = alice_position[1] + directions[command][1]

    if not (0<= new_row < size and 0<= new_col< size):
        break

    alice_position = [new_row, new_col]

    if matrix[new_row][new_col] == 'R':
            matrix[new_row][new_col] = '*'
            break

    if matrix[new_row][new_col].isdigit():
        collected_tea_bags += int(matrix[new_row][new_col])

    matrix[new_row][new_col] = '*'

if collected_tea_bags < 10:
    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")

print(*(" ".join(el) for el in matrix), sep = '\n')