def grocery_store(**kwargs):
    for key, value in kwargs.items():
        result = dict(sorted(kwargs.items(), key=lambda x: (-(x[1]), -len(x[0]), x[0])))
    my_list = []
    for key, value in result.items():
        my_list.append(f"{key}: {value}")

    return '\n'.join(my_list)


# Another way
#
#
# def grocery_store(**kwargs):
#     result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#
#     return '\n'.join(f"{product}: {quantity}" for product, quantity in result)
