from collections import deque

data = deque(input().split())

colors = {'yellow', 'red', 'blue', 'orange', 'green', 'purple'}

my_dict_colors = {
    'orange': {'red', 'yellow'},
    'green': {'yellow', 'blue'},
    'purple': {'blue', 'red'}
}
result = []

while data:
    first_word = data.popleft()
    second_word = data.pop() if data else ''

    for word in (first_word + second_word, second_word + first_word):
        if word in colors:
            result.append(word)
            break

    else:
        for el in(first_word[:-1],second_word[:-1]):
            if el:
                data.insert(len(data)//2,el)

for color in set(my_dict_colors.keys()).intersection(result):
    if not my_dict_colors[color].issubset(result):
        result.remove(color)

print(result)
