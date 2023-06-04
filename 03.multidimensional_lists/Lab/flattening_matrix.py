
rows = int(input())
matrix = []
flatten = []

for row_index in range(rows):
    inner_list = [int(el) for el in input().split(', ')]
    matrix.append(inner_list)

for el in matrix:
    flatten.extend(el)

print(flatten)

# 2nd way
#
# rows = int(input())
#
# flatten = []
#
# for row_index in range(rows):
#     inner_list = [int(el) for el in input().split(', ')]
#     flatten.extend(inner_list)
#
# print(flatten)



