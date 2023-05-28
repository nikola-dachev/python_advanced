n = int(input())

max_intersect = set()

for _ in range(n):
    first_command, second_command = input().split('-')
    first_start, first_end = first_command.split(',')
    second_start, second_end = second_command.split(',')

    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))

    intersec = first_set.intersection(second_set)
    if len(intersec) > len(max_intersect):
        max_intersect = intersec

print(f"Longest intersection is [{', '.join([str(el) for el in max_intersect])}] with length {len(max_intersect)}")
