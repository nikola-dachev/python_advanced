from collections import deque

customers = deque()

while True:
    command = input()
    if command != 'Paid' and command != 'End':
        customers.append(command)

    elif command == 'Paid':
        while len(customers) != 0:
            print(customers.popleft())

    elif command == 'End':
        print(f'{len(customers)} people remaining.')
        break


