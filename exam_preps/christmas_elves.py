from collections import deque

total_energy = 0
total_toys = 0
counter = 0

elves_energy = deque([int(el) for el in input().split()])
materials = deque([int(el) for el in input().split()])

while elves_energy and materials:

    current_elf = elves_energy.popleft()
    material = materials[-1]

    if current_elf < 5:
        continue

    counter += 1
    current_toy_count = 0

    if counter % 3 == 0:
        material *= 2
        current_toy_count += 1

    if current_elf >= material:
        total_energy += material
        current_elf -= material

        if counter % 5 != 0:
            current_toy_count += 1
            current_elf += 1

        else:
            current_toy_count = 0

        materials.pop()

    else:
        current_elf *= 2
        current_toy_count = 0

    total_toys += current_toy_count
    elves_energy.append(current_elf)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if elves_energy:
    print(f"Elves left: {', '.join([str(el) for el in elves_energy])}")

else:
    print(f"Boxes left: {', '.join([str(el) for el in materials])}")
