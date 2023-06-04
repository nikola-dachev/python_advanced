from collections import deque
from datetime import datetime , timedelta

robot_list = input().split(';')
robot_dict = {}

for r in robot_list:
    current_command = r.split('-')
    robot_name = current_command[0]
    time_needed = int(current_command[1])
    robot_dict[robot_name]= [time_needed , 0]

factory_time = datetime.strptime(input(), '%H:%M:%S')

products = deque()

while True:
    product = input()

    if product == 'End':
        break
    products.append(product)

while products:
    factory_time +=timedelta(0,1) # 0 is for day , 1 for seconds
    product = products.popleft()

    free_robots = []
    for name, value in robot_dict.items():
        if value[1] != 0:
            robot_dict[name][1] -=1
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name , data = free_robots[0]
    robot_dict[robot_name][1]= data[0]

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")



