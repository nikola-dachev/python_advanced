first_sequence = set([int(el) for el in input().split()])
second_sequence = set([int(el) for el in input().split()])

number_of_lines = int(input())

for line in range(number_of_lines):
  command = input().split()
  action = command[0]
  action_sequence = command[1]
  numbers = [int(el) for el in command[2:]]

  if action == 'Add' and action_sequence == 'First':
    for el in numbers:
      first_sequence.add(el)
  elif action == 'Add' and action_sequence == 'Second':
    for el in numbers:
      second_sequence.add(el)

  elif action == 'Remove' and action_sequence == 'First':
    for el in numbers:
      if el in first_sequence:
        first_sequence.remove(el)

  elif action == 'Remove' and action_sequence == 'Second':
    for el in numbers:
      if el in second_sequence:
        second_sequence.remove(el)

  elif action == 'Check' and action_sequence == 'Subset':
    if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
      print('True')
    else:
      print('False')

first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)
print(*first_sequence, sep = ', ')
print(*second_sequence, sep = ', ')