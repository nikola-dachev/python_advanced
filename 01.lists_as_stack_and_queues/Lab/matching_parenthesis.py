stack_index = []
text = input()

for index in range(len(text)):
  if text[index] == '(':
    stack_index.append(index)

  elif text[index]==')':
    start_position = stack_index.pop()
    end_index = index +1
    print(text[start_position:end_index])