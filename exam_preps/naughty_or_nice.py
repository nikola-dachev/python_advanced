def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids_list = []
    naughty_kids_list = []
    result = []

    def place_in_a_list():
        if len(kid) == 1:
            # we check if the len is only 1 so to process it otherwise we ignore the command
            nice_kids_list.extend(kid) if type_of_kid == 'Nice' else naughty_kids_list.extend(kid)

            santa_list.remove(*kid)

    for arg in args:
        number, type_of_kid = arg.split('-')
        # this gives you a tuple of all kids with the particular number
        kid = [info for info in santa_list if info[0] == int(number)]
        place_in_a_list()

    for name, type_of_kid in kwargs.items():
        # this gives you a tuple of all kids with the particular number
        kid = [info for info in santa_list if info[1] == name]
        place_in_a_list()

    if nice_kids_list:
        result.append(f"Nice: {', '.join(k[1] for k in nice_kids_list)}")

    if naughty_kids_list:
        result.append(f"Naughty: {', '.join(k[1] for k in naughty_kids_list)}")

    if santa_list:
        result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
    "3-Nice", "1-Naughty",
    Amy="Nice", Katy="Naughty", ))
