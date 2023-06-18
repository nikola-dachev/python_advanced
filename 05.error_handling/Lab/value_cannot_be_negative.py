class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        number = float(input('Pass a number:'))
        if number < 0:
            raise ValueCannotBeNegative

    except ValueError:
        print('This is not a number')
