from collections import deque

bees = deque(int(el) for el in input().split())
nectars = deque(int(el) for el in input().split())
symbols = deque(input().split())

total_honey = 0

while bees and nectars:
    current_bee = bees.popleft()
    current_nectar = nectars.pop()
    current_symbol = symbols.popleft()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        symbols.appendleft(current_symbol)
        continue

    if current_nectar > current_bee:
        if current_symbol == '*':
            total_honey += abs(current_bee * current_nectar)
        elif current_symbol =='/':
            total_honey += abs(current_bee / current_nectar)
        elif current_symbol == '-':
            total_honey += abs(current_bee - current_nectar)
        elif current_symbol == '+':
            total_honey += abs(current_bee + current_nectar)

print(f'Total honey made: {total_honey}')

if bees:
    print(f'Bees left: {", ".join([str(el) for el in bees])}')

if nectars:
    print(f"Nectar left: {', '.join(str(el) for el in nectars)}")