number_of_guests = int(input())

my_set = set()

for guest in range(number_of_guests):
  command = input()
  my_set.add(command)

while True:
  command = input()

  if command == 'END':
    break

  if command in my_set:
    my_set.remove(command)

print(len(my_set))
for el in sorted(my_set):
  print(el)

