from collections import deque

caffeine = deque([int(el) for el in input().split(', ')])
energy_drinks = deque([int(el) for el in input().split(', ')])

initial_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    result = current_caffeine * current_energy_drink
    if initial_caffeine + result <= 300:
        initial_caffeine += result

    else:
        energy_drinks.append(current_energy_drink)
        initial_caffeine -= 30

        if initial_caffeine < 0:
            initial_caffeine = 0

if not energy_drinks:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

if energy_drinks:
    print(f"Drinks left: {', '.join([str(el) for el in energy_drinks])}")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")


