rows,cols = [int(el) for el in input().split(', ')]
matrix = []

for _ in range( rows):
  inner_list = [int(el) for el in input().split(', ')]
  matrix.append(inner_list)

max_sum_matrix = -float('inf')
position_first_row = None
position_second_row = None

for row_index in range(rows-1):
  for col_index in range(cols-1):
    current_element = matrix[row_index][col_index]
    element_below = matrix[row_index+1][col_index]
    next_element = matrix[row_index][col_index+1]
    diagonal_element = matrix[row_index +1][col_index+1]
    total_sum = current_element + element_below + next_element + diagonal_element
    if total_sum >max_sum_matrix:
      max_sum_matrix = total_sum
      position_first_row = (current_element,next_element)
      position_second_row = (element_below, diagonal_element)

print(*position_first_row)
print(*position_second_row)
print(max_sum_matrix)
