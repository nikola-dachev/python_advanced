number_of_students = int(input())
my_dict = {}

for _ in range(number_of_students):
    command = input().split()
    name = command[0]
    grade = float(command[1])

    if name not in my_dict:
        my_dict[name] = []

    my_dict[name].append(grade)

for name, value in my_dict.items():
    average_score = sum(my_dict[name]) / len(my_dict[name])
    print(f'{name} -> {" ".join([str(f"{el:.2f}") for el in value])} (avg: {average_score:.2f})')


