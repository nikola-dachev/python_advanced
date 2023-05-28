n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    total_sum = 0

    for char in name:
        total_sum += ord(char)

    total_sum //= row

    if total_sum % 2 == 0:
        even_set.add(total_sum)

    else:
        odd_set.add(total_sum)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')

else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')