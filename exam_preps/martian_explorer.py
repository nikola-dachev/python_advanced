SIZE = 6
matrix = []
rover_position = []

deposits = {
    'W': ['Water', 0],
    'M': ['Metal', 0],
    'C': ['Concrete', 0]
}

directions = {
    'up': lambda r, c: [(r - 1) % SIZE, c],
    'down': lambda r, c: [(r + 1) % SIZE, c],
    'left': lambda r, c: [r, (c - 1) % SIZE],
    'right': lambda r, c: [r, (c + 1) % SIZE]
}

for row in range(SIZE):
    current_row = input().split()

    if 'E' in current_row:
        rover_position = [row, current_row.index('E')]

    matrix.append(current_row)

commands = input().split(', ')

for command in commands:
    rover_position = directions[command](*rover_position)
    # position shows you what you have found on the new rover positions - W,C, M etc
    position = matrix[rover_position[0]][rover_position[1]]

    if position in deposits:
        print(f"{deposits[position][0]} deposit found at ({rover_position[0]}, {rover_position[1]})")

        deposits[position][1] += 1

    elif position == 'R':
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
        break

if all([deposits['W'][1], deposits['M'][1], deposits['C'][1]]):
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
