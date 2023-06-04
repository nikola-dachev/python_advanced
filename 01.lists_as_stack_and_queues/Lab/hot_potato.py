from collections import deque

names = deque(input().split())

rotations = int(input())

while len(names)!=1:
  rotation_number = rotations -1 # we want to pop the person before the end of the rotation
  names.rotate(-rotation_number) #we rotate from left to right that's why it is -rotation_number
  kid = names.popleft()
  print(f"Removed {kid}")

print(f"Last is {names.popleft()}")