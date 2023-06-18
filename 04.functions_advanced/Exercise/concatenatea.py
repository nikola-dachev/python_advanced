def concatenate(*args, **kwargs):
    final_string = ''
    for el in args:
        final_string += el
    for key, value in kwargs.items():
        if key in final_string:
            final_string = final_string.replace(key, value)

    return final_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
