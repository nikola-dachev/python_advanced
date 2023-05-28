from collections import OrderedDict

text = input()
my_dict = {}

for char in text:
  if char not in my_dict:
    my_dict[char] = 0

  my_dict[char]+=1

my_dict = OrderedDict(sorted(my_dict.items()))

for key, value in my_dict.items():
  print(f'{key}: {value} time/s')