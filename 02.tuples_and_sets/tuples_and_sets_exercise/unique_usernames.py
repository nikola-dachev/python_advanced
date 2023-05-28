number_usernames = int(input())
my_set = set()

for _ in range(number_usernames):
    username = input()
    my_set.add(username)

for el in my_set:
    print(el)
