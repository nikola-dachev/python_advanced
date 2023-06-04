rows, cols = [int(el) for el in input().split(', ')]
matrix = []

for row in range(rows):
  inner_list = [int(el) for el in input().split()]
  matrix.append(inner_list)


for col_index in range(cols):
  sum = 0
  for row_index in range(rows):
    sum +=matrix[row_index][col_index]
  print(sum)
