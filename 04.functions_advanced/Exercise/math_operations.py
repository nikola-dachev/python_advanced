def math_operations(*args, **kwargs):
    for i in range(len(args)):
        key = list(kwargs.keys())[i % 4]

        if key == 'a':
            kwargs[key] += args[i]

        elif key == 's':
            kwargs[key] -= args[i]

        elif key == 'd':
            if args[i] != 0:
                kwargs[key] /= args[i]

        elif key == 'm':
            kwargs[key] *= args[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join([f"{letter}: {number:.1f}" for letter, number in kwargs])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
