from collections import deque

monsters_armour = deque([int(el) for el in input().split(',')])
strenght_of_strikes = deque([int(el) for el in input().split(',')])
monsters_killed = 0

while monsters_armour and strenght_of_strikes:
    current_monster_armour = monsters_armour.popleft()
    current_strike = strenght_of_strikes.pop()

    if current_strike >= current_monster_armour:
        current_strike -= current_monster_armour
        monsters_killed += 1

        if current_strike > 0:
            if len(strenght_of_strikes) > 0:
                strenght_of_strikes[-1] += current_strike
            else:
                strenght_of_strikes.append(current_strike)

    else:
        current_monster_armour -= current_strike
        monsters_armour.append(current_monster_armour)

if not monsters_armour:
    print("All monsters have been killed!")

if not strenght_of_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
