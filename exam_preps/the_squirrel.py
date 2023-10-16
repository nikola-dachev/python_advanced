size = int(input())
given_directions = input().split(', ')

matrix = []
directions = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0, 1)
}
squirrel_position = ()
collected_hazelnuts = 0

for row in range(size):
    inner_list = list(input())
    matrix.append(inner_list)

    if 's' in inner_list:
        squirrel_position = (row, inner_list.index('s'))
        matrix[squirrel_position[0]][squirrel_position[1]] = '*'


for direction in given_directions:
    new_row = squirrel_position[0] + directions[direction][0]
    new_col = squirrel_position[1] + directions[direction][1]

    if not (0<= new_row <size and 0<= new_col < size):
        print("The squirrel is out of the field.")
        break

    if matrix[new_row][new_col] == 'h':
        collected_hazelnuts +=1
        matrix[new_row][new_col] = '*'
        if collected_hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    if matrix[new_row][new_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    squirrel_position = (new_row, new_col)

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")

