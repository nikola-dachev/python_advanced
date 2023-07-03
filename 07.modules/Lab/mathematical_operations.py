def sum_nums(num_1, num_2):
    return num_1 + num_2

def multiply_nums(num_1, num_2):
    return num_1 * num_2

def subtract_nums(num_1, num_2):
    return num_1 - num_2

def divide_nums(num_1, num_2):
    return num_1 / num_2

def pow_nums(num_1, num_2):
    return num_1 ** num_2

mapper = {
    '+': sum_nums,
    '-': subtract_nums,
    '/': divide_nums,
    '*': multiply_nums,
    '^': pow_nums
}

def execute_string(expression):
    num_1 , sign, num_2 = expression.split()
    num_1 = float(num_1)
    num_2 = int(num_2)

    return f'{(mapper[sign](num_1, num_2)):.2f}'

print(execute_string('36.66 / 6'))