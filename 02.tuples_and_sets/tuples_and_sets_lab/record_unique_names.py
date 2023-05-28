n = int(input())

my_set = set()

for _ in range(n):
  name = input()
  my_set.add(name)

for el in my_set:
  print(el)