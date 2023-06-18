def func_executor(*args):
  final_result = []
#func is the name of the function- i.e. some_numbers , arg is the tuple of the parameters of the function - i.e num1, num2
  for func, arg in args:
    final_result.append(f"{func.__name__} - {func(*arg)}")

  return '\n'.join(final_result)

def sum_numbers(num1, num2):
  return num1 + num2
def multiply_numbers(num1, num2):
  return num1 * num2

print(func_executor( (sum_numbers, (1, 2)), (multiply_numbers, (2, 4)) ))
