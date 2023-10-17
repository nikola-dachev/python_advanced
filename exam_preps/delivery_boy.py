rows, cols = [int(el) for el in input().split()]

matrix = []

directions = {
  'up': (-1, 0),
  'down': (1, 0),
  'left': (0, -1),
  'right': (0, 1)
}
boy_position = ()

for row in range(rows):
  inner_list = list(input())
  matrix.append(inner_list)

  if 'B' in inner_list:
    boy_position = (row, inner_list.index('B'))
    starting_position = (row, inner_list.index('B'))

direction = input()
while direction:
  new_row = boy_position[0] + directions[direction][0]
  new_col = boy_position[1] + directions[direction][1]

  if not(0<=new_row < rows and 0<=new_col< cols):
    matrix[starting_position[0]][starting_position[1]] = ' '
    print("The delivery is late. Order is canceled.")
    break

  if matrix[new_row][new_col] == 'P':
    matrix[new_row][new_col] = 'R'
    print("Pizza is collected. 10 minutes for delivery.")

  if matrix[new_row][new_col] == '*':
    new_row = boy_position[0]
    new_col = boy_position[1]

  if matrix[new_row][new_col] == 'A':
    matrix[new_row][new_col] = 'P'
    print("Pizza is delivered on time! Next order...")
    break

  if matrix[new_row][new_col] == '-':
    matrix[new_row][new_col] = '.'

  boy_position = (new_row, new_col)
  direction = input()

for row in matrix:
  print(*row, sep = '')
