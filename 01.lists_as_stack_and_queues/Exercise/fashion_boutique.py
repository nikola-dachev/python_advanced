from collections import deque

clothes = deque([int(el) for el in input().split()])
shelf_capacity = int(input())

shelf_counter = 1
current_shelf_capacity = shelf_capacity

while clothes:
    cloth = clothes.pop()

    if current_shelf_capacity >= cloth:
        current_shelf_capacity -= cloth


    else:
        shelf_counter += 1
        current_shelf_capacity = shelf_capacity - cloth

print(shelf_counter)

