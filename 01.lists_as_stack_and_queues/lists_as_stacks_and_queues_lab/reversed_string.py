text = input()
stacked_list = list(text)
removed_elements = ''

while len(stacked_list) !=0:
  removed_elements +=stacked_list.pop()

print(f'{removed_elements}')