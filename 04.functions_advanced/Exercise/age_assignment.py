
def age_assignment(*args, **kwargs):
    my_list = []
    for key, value in sorted(kwargs.items(), key=lambda x: x[0]):
        for name in args:
            if name[0] == key:
                my_list.append(f"{name} is {value} years old.")

    return '\n'.join(my_list)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# Another way
#
#
# def age_assignment(*args, **kwargs):
#     my_list = []
#     for key, value in kwargs.items():
#         for name in args:
#             if name[0] == key:
#                 my_list.append(f"{name} is {value} years old.")
#
#     return '\n'.join(sorted(my_list))
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
