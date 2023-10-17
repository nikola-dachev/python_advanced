from collections import deque

times_needed = deque([int(el) for el in input().split()])
number_of_tasks = deque([int(el) for el in input().split()])

duck_dictionary = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while times_needed and number_of_tasks:
    current_time = times_needed.popleft()
    current_task = number_of_tasks.pop()

    current_result = current_time * current_task

    if 0 <= current_result <= 60:
        duck_dictionary['Darth Vader Ducky'] += 1

    elif 61 <= current_result <= 120:
        duck_dictionary['Thor Ducky'] += 1

    elif 121 <= current_result <= 180:
        duck_dictionary['Big Blue Rubber Ducky'] += 1

    elif 181 <= current_result <= 240:
        duck_dictionary['Small Yellow Rubber Ducky'] += 1

    elif current_result > 240:
        current_task -= 2
        times_needed.append(current_time)
        number_of_tasks.append(current_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in duck_dictionary.items():
    print(f"{key}: {value}")



