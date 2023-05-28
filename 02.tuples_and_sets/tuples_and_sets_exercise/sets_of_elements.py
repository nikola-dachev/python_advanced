data= input().split()
n = int(data[0])
m = int(data[1])
n_set = set()
m_set = set()

for _ in range(n):
  num = int(input())
  n_set.add(num)

for _ in range(m):
  num = int(input())
  m_set.add(num)

unique_el = n_set.intersection(m_set)
for el in unique_el:
  print(el)

