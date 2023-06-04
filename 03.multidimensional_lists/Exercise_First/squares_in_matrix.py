rows, cols = [int(el) for el in input().split()]
matrix = []
counter = 0

for _ in range(rows):
  inner_list = [el for el in input().split()]
  matrix.append(inner_list)

for row_index in range(rows-1):
  for col_index in range(cols-1):
    current_element = matrix[row_index][col_index]
    next_element = matrix[row_index][col_index+1]
    below_element = matrix[row_index +1][col_index]
    diagonal_element = matrix[row_index +1][col_index +1]
    if current_element == next_element == below_element == diagonal_element:
      counter+=1

print(counter)

