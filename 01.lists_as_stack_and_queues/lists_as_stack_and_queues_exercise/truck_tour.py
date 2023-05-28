from collections import deque

number_petrol_stations = int(input())
petrol_pumsp_deque = deque()

for _ in range(number_petrol_stations):
    command = [int(el) for el in input().split()]
    petrol_pumsp_deque.append(command)

gas_in_tank = 0
index = 0

petrol_pumsp_deque_copy = petrol_pumsp_deque.copy()

while petrol_pumsp_deque_copy:
    petrol, distance = petrol_pumsp_deque_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -=distance

    else:
        petrol_pumsp_deque.rotate(-1)
        petrol_pumsp_deque_copy = petrol_pumsp_deque.copy()
        index +=1
        gas_in_tank =0

print(index)