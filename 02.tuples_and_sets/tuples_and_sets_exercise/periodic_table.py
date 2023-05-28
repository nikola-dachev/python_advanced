number_of_elements = int(input())
my_set = set()
for _ in range(number_of_elements):
  command = input().split()
  for el in command:
    my_set.add(el)

for el in my_set:
  print(el)