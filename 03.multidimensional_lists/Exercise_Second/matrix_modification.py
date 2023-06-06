rows = int(input())
matrix =[]

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

while True:
    command = input()
    if command =='END':
        break

    current_command = command.split()
    action = current_command[0]
    row = int(current_command[1])
    col = int(current_command[2])
    value = int(current_command[3])

    if not (0<=col<= len(matrix)- 1 and 0<=row <= len(matrix)):
        print("Invalid coordinates")
        continue

    if action == 'Add':
        matrix[row][col] += value

    elif action =='Subtract':
        matrix[row][col] -= value

for el in matrix:
    print(*el)