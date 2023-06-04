rows = int(input())
matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

primary_diagonal = []
secondary_diagonal = []

for row_index in range(rows):
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][rows - row_index - 1])

diagonal_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diagonal_difference)
