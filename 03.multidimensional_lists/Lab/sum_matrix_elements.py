rows, cols = [int(el) for el in input().split(', ')]
matrix = []
total_sum = 0

for row in range(rows):
    inner_list = [int(el) for el in input().split(', ')]
    matrix.append(inner_list)

for row_index in range(rows):
    for col_index in range(cols):
        total_sum += matrix[row_index][col_index]

print(total_sum)
print(matrix)

# 2nd way
# rows, cols = [int(el) for el in input().split(', ')]
# matrix = []
# total_sum = 0
#
# for row in range(rows):
#     inner_list = [int(el) for el in input().split(', ')]
#     total_sum += sum(inner_list)
#     matrix.append(inner_list)
#
# print(total_sum)
# print(matrix)
