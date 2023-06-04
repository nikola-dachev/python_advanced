from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = deque([int(el) for el in input().split()])

wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()

    if cup <= bottle:
        wasted_water += bottle - cup

    else:
        cups.appendleft(cup - bottle)

if bottles:
    print(f"Bottles: {' '.join([str(el) for el in bottles])}")

else:
    print(f"Cups: {' '.join([str(el) for el in cups])}")

print(f'Wasted litters of water: {wasted_water}')