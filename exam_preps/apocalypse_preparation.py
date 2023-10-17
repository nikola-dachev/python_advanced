from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = deque([int(el) for el in input().split()])

my_dict = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    result = current_textile + current_medicament

    if result == 30:
        my_dict['Patch'] +=1

    elif result == 40:
        my_dict['Bandage'] +=1

    elif result == 100:
        my_dict['MedKit'] += 1

    elif result > 100:
        my_dict['MedKit'] +=1
        result -= 100
        medicaments[-1] += result

    else:
        current_medicament +=10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

sorted_dict = sorted(my_dict.items(), key = lambda x: (-(x[1]),x[0]))
for key , value in sorted_dict:
    if value >0:
        print(f'{key} - {value}')

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join([str(el) for el in medicaments])}")
if textiles:
    print(f"Textiles left: {', '.join([str(el) for el in textiles])}")


