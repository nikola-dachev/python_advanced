from collections import deque

def fill_the_box(height, length, width, *args):
    space = height * length * width
    args = deque(args)

    while args[0] != 'Finish':
        number = args.popleft()
        space -= number

        if space < 0:
            cubes_left = sum(el for el in args if el != 'Finish')
            return f"No more free space! You have {cubes_left + abs(space)} more cubes."

    return f"There is free space in the box. You could put {space} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
