from collections import deque

water_quantity = int(input())
queue_list = deque()

while True:
    command = input()

    if command == 'Start':
        break

    queue_list.append(command)

while True:
    command = input()

    if command == 'End':
        print(f"{water_quantity} liters left")
        break

    current_command = command.split()
    if len(current_command) == 1:
        requested_water = int(current_command[0])

        if water_quantity >= requested_water:
            water_quantity -= requested_water
            person = queue_list.popleft()
            print(f"{person} got water")

        else:
            person = queue_list.popleft()
            print(f"{person} must wait")

    else:  # current_command is refill qty
        water_quantity += int(current_command[1])

