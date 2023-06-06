
data = input().split("|")
my_list = []

for el in data[::-1]:
    new_el = el.split()
    my_list.extend(new_el)

print(*my_list)