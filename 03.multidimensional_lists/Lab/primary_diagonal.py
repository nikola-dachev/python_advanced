rows = int(input())
matrix = []
diagonal_sum = 0

for _ in range(rows):
  inner_list = [int(el) for el in input().split()]
  matrix.append(inner_list)

for row_index in range(rows):
  diagonal_sum += matrix[row_index][row_index]

print(diagonal_sum)
