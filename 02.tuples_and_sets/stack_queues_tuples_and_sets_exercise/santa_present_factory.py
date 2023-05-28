from collections import deque

materials = deque(int(el) for el in input().split())
magic_numbers = deque(int(el) for el in input().split())

result = []
presents = {
    150 : 'Doll',
    250 : 'Wooden train',
    300 : 'Teddy bear',
    400 : 'Bicycle'
}
while materials and magic_numbers:
    current_material= materials.pop()
    current_magic_number = magic_numbers.popleft()

    total_magic_level = current_magic_number * current_material

    if current_material== 0 and current_magic_number== 0:
        continue

    if current_material == 0:
        magic_numbers.appendleft(current_magic_number)

    if current_magic_number == 0:
        materials.append(current_material)

    if presents.get(total_magic_level): # we do not say prents[total_magic_level] because if the result is something different form the values we need we will get an error

        result.append(presents[total_magic_level])

    elif total_magic_level < 0:
        materials.append(current_material + current_magic_number)

    elif total_magic_level > 0:
        materials.append(current_material + 15)

if {'Wooden train', 'Doll'}.issubset(result) or {'Bicycle', 'Teddy Bear'}.issubset(result):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join([str(el)for el in materials][::-1])}')

if magic_numbers:
    print(f'"Magic left: {", ".join(str(el) for el in magic_numbers)}')

[print(f'{toy}: {result.count(toy)}') for toy in sorted(set(result))]