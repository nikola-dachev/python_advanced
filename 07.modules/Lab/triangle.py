size = int(input())

for row in range(1, size +1):
    for num in range(1,row):
        print(num, end=' ')
    print()

for row in range(size-1, 1, -1):
    for num in range(1,row):
        print(num, end= ' ')
    print()