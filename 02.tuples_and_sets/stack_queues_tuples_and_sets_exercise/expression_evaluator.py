from collections import deque
from math import floor

data = deque(input().split())

index = 0

while index < len(data):
    element = data[index]

    if element == '*':
        for _ in range(index - 1):
            data.appendleft(int(data.popleft()) * int(data.popleft()))

    elif element == '+':
        for _ in range(index - 1):
            data.appendleft(int(data.popleft()) + int(data.popleft()))

    elif element == '-':
        for _ in range(index - 1):
            data.appendleft(int(data.popleft()) - int(data.popleft()))

    elif element == '/':
        for _ in range(index - 1):
            data.appendleft(int(data.popleft()) / int(data.popleft()))

    if element in '*/+-':
        del data[1]
        index = 0

    index += 1

print(floor(int(data[0])))
