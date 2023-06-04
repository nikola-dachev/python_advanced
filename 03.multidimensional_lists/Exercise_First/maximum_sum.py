rows, cols = [int(el) for el in input().split()]
matrix = []

biggest_matrix = []
for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

max_sum = -float('inf')

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        first_row = matrix[row_index][col_index:col_index + 3]
        second_row = matrix[row_index + 1][col_index:col_index + 3]
        third_row = matrix[row_index + 2][col_index:col_index + 3]

        total_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if total_sum > max_sum:
            max_sum = total_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")

# rows in the biggest matrix are first_row, second_row and third_row
for row in biggest_matrix:
    print(*row)
