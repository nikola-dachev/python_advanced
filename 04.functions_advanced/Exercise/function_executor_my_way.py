def func_executor(*args):
    list_result = []
    for function_name, parameters in args:
        list_result.append(f"{function_name.__name__} - {function_name(*parameters)}")
    return '\n'.join(list_result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
