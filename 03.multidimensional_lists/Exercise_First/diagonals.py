rows = int(input())
matrix = []

for _ in range(rows):
  inner_list = [int(el) for el in input().split(', ')]
  matrix.append(inner_list)

primary_diagonal = 0
secondary_diagonal = 0
position_primary = []
position_secondary = []

for row_index in range(rows):
  primary_diagonal +=matrix[row_index][row_index]
  secondary_diagonal +=matrix[row_index][rows - row_index - 1]
  position_primary.append(matrix[row_index][row_index])
  position_secondary.append(matrix[row_index][rows - row_index - 1])

print(f"Primary diagonal: {', '.join(str(el)for el in position_primary)}. Sum: {primary_diagonal}")

print(f"Secondary diagonal: {', '.join(str(el) for el in position_secondary)}. Sum: {secondary_diagonal}")
