from collections import deque

chocolates = deque([int(el) for el in input().split(', ')])
cups_milk = deque([int(el) for el in input().split(', ')])
milkshakes = 0

while chocolates and cups_milk and milkshakes != 5:

    current_chocolate = chocolates.pop()
    current_cup_milk = cups_milk.popleft()

    if current_chocolate <= 0 and current_cup_milk <= 0:
        continue

    elif current_chocolate <= 0:
        cups_milk.appendleft(current_cup_milk)
        continue

    elif current_cup_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup_milk:
        milkshakes += 1

    else:
        cups_milk.append(current_cup_milk)
        chocolates.append(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

if len(chocolates) != 0:
    print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join([str(el) for el in cups_milk])}")
else:
    print("Milk: empty")
