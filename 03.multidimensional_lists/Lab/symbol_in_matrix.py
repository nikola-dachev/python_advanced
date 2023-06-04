n = int(input())

matrix = []

for _ in range(n):
  inner_list = list(input())
  matrix.append(inner_list)

special_symbol = input()
position = None

for row_index in range(n):
  if position:
    break
  for col_index in range(n):
    if matrix[row_index][col_index] == special_symbol:
      position = (row_index, col_index)
      break

if position:
  print(position)

else:
  print(f"{special_symbol} does not occur in the matrix")

