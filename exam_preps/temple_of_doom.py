from collections import deque

tools = deque([int(el) for el in input().split()])
substances = deque([int(el) for el in input().split()])
challenges = deque([int(el) for el in input().split()])

while substances and challenges:

  current_tool = tools.popleft()
  current_substance = substances.pop()
  force = current_tool * current_substance

  for el in challenges:
    if force == el:
      current_challenge = challenges.remove(el)
      break

  else:
    current_tool += 1
    tools.append(current_tool)
    current_substance -= 1
    if current_substance > 0:
      substances.append(current_substance)



if not challenges:
  print("Harry found an ostracon, which is dated to the 6th century BCE.")

else:
  print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
  print("Tools: ", end= '')
  print(*tools, sep=', ')

if substances:
  print("Substances: ", end= '')
  print(*substances, sep=', ')

if challenges:
  print("Challenges: ", end= '')
  print(*challenges, sep=', ')

