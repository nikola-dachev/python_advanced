my_list = input().split()
stacked_list = []

while len(my_list) != 0:
  removed_el = my_list.pop()
  stacked_list.append(removed_el)

print(' '.join(stacked_list))