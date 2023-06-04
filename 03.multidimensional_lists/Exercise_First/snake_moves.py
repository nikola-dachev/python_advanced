#With List Comprehension

from collections import deque

rows, cols = [int(el) for el in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(rows):
  while len(word_copy)< cols:
    word_copy.extend(word)

  if row % 2 == 0:
    print(*[word_copy.popleft() for _ in range(cols)], sep='')
  else:
    print(*[word_copy.popleft() for _ in range(cols)][::-1], sep ='')


# Without List Comprehension
# from collections import deque
#
# rows, cols = [int(el) for el in input().split()]
# word = list(input())
#
# word_copy = deque(word)
#
# for row in range(rows):
#   while len(word_copy)< cols:
#     word_copy.extend(word)
#
#   letter_list =[]
#   if row % 2 == 0:
#     for _ in range(cols):
#       letter_list.append(word_copy.popleft())
#     print(*letter_list,sep='')
#   else:
#     for _ in range(cols):
#       letter_list.append(word_copy.popleft())
#     print(*letter_list[::-1], sep= '')
