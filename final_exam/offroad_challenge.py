from collections import deque

initial_fuel = deque([int(el) for el in input().split()])
additional_consumption_indexes = deque([int(el) for el in input().split()])
fuel_needed = deque([int(el) for el in input().split()])

counter_altitudes = 0
counter_index = 0

while initial_fuel and additional_consumption_indexes:
    current_initial_fuel = initial_fuel.pop()
    current_additional_consumption_index = additional_consumption_indexes.popleft()
    current_fuel_needed = fuel_needed.popleft()

    counter_index +=1
    result = current_initial_fuel - current_additional_consumption_index

    if result >= current_fuel_needed:
        counter_altitudes += 1
        print(f"John has reached: Altitude {counter_altitudes}")

    else:
        print(f"John did not reach: Altitude {counter_index}")
        break

if counter_altitudes == 4:
    print("John has reached all the altitudes and managed to reach the top!")

elif counter_altitudes == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

else:
    print("John failed to reach the top.")
    print("Reached altitudes: ", end='')
    print(', '.join([f"Altitude {str(number)}" for number in range(1,counter_altitudes +1)]))
