from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())

bullets = deque([int(bullet) for bullet in input().split()])
locks = deque([int(lock) for lock in input().split()])

treasure_value = int(input())

shots_bullets = 0
bullets_in_barrel = gun_barrel_size

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_lock >= current_bullet:
        print("Bang!")

    else:
        locks.appendleft(current_lock)
        print( "Ping!")

    shots_bullets +=1
    bullets_in_barrel -=1

    if bullets_in_barrel ==0 and len(bullets) !=0:

        if gun_barrel_size < len(bullets):
            bullets_in_barrel = gun_barrel_size
        else:
            bullets_in_barrel = len(bullets)
        print("Reloading!")


total_expenses = bullet_price * shots_bullets
money_earned = treasure_value  - total_expenses

if len(locks) != 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")

else:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")