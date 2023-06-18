def even_odd(*args):
    command = args[-1]
    odd_list = []
    even_list = []

    for el in args[:-1]:
        if el % 2 == 0:
            even_list.append(el)

        elif el % 2 != 0:
            odd_list.append(el)

    if command == 'even':
        return even_list
    elif command == 'odd':
        return odd_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

