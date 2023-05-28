from collections import deque

n = int(input())

final_deque = deque()

map_functions = {
    1: lambda x: final_deque.append(x[1]),
    2: lambda x: final_deque.pop() if final_deque else None,
    3: lambda x: print(max(final_deque)) if final_deque else None,
    4: lambda x: print(min(final_deque)) if final_deque else None
}

for _ in range(n):
    command = [int(num) for num in input().split()]

    map_functions[command[0]](command)

final_deque.reverse()
print(*final_deque, sep=', ')


#or
# from collections import deque
#
# n = int(input())
#
# final_deque = deque()
#
# for _ in range(n):
#     command = [int(num) for num in input().split()]
#
#     action = command[0]
#
#     if action == 1:
#         final_deque.append(command[1])
#
#     elif action == 2:
#         if final_deque:
#             final_deque.pop()
#
#     elif action == 3:
#         if final_deque:
#             print(max(final_deque))
#
#     elif action == 4:
#         if final_deque:
#             print(min(final_deque))
# final_deque.reverse()
# print(*final_deque, sep=', ')