number_of_cars = int(input())

my_set = set()

for car in range(number_of_cars):
  command = input().split(", ")
  action = command[0]
  plate = command[1]

  if action =='IN':
    my_set.add(plate)

  elif action == 'OUT':
    my_set.remove(plate)

if len(my_set) == 0:
  print(f"Parking Lot is Empty")

else:
  for el in my_set:
    print(el)