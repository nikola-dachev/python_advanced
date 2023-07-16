
def words_sorting(*args):
    my_dict = {}
    asci_sum = 0

    for arg in args:
        for char in arg:
            asci_sum += ord(char)
        my_dict[arg] = asci_sum
        asci_sum = 0

    result = []

    if sum(my_dict.values()) % 2 == 0:
        for key, value in sorted(my_dict.items(), key=lambda x: x[0]):
            result.append(f'{key} - {value}')
    else:
        for key, value in sorted(my_dict.items(), key=lambda x: -x[1]):
            result.append(f'{key} - {value}')

    return '\n'.join(result)


# with MAP
#
#
# def words_sorting(*args):
#     my_dict = {arg: sum(map(ord, arg)) for arg in args}
#     result = []
#
#     if sum(my_dict.values()) % 2 == 0:
#         for key, value in sorted(my_dict.items(), key=lambda x: x[0]):
#             result.append(f'{key} - {value}')
#     else:
#         for key, value in sorted(my_dict.items(), key=lambda x: (-x[1])):
#             result.append(f'{key} - {value}')
#
#     return '\n'.join(result)
