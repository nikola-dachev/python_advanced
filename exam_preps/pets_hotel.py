def accommodate_new_pets(capacity, max_weight, *args):
    my_dict = {}
    final_result = ''

    for pet_type, pet_weight in args:
        if pet_type not in my_dict:
            my_dict[pet_type] = 0

    for pet_type, pet_weight in args:

        if capacity == 0:
            final_result +=  "You did not manage to accommodate all pets!" + '\n'
            break

        if pet_weight <= max_weight:
            my_dict[pet_type] += 1
            capacity -= 1

        elif pet_weight > max_weight:
            continue

    else:
        final_result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    sorted_dict = sorted(my_dict.items(), key = lambda x: x[0])
    final_result += "Accommodated pets:\n"
    for animal, number in sorted_dict:
        if number >0:
            final_result += f'{animal}: {number}\n'

    return final_result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

