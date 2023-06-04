1st way

rows = int(input())
matrix = []
for row_index in range(rows):
  inner_list = [int(el) for el in input().split(', ')]
  even_list = []
  for el in inner_list:
    if el % 2  == 0:
      even_list.append(el)
  matrix.append(even_list)

print(matrix)

# 2nd way
#
# rows = int(input())
# matrix = []
#
# for row_index in range(rows):
#   inner_list = [int(el) for el in input().split(', ')]
#   even_list = [el for el in inner_list if el % 2 == 0]
#   matrix.append(even_list)
#
# print(matrix)
