def get_info(name,town,age):
  return f"This is {name} from {town} and he is {age} years old"

my_dict={'name':'az', 'town':'Sofia', 'age':25}

print(get_info(**my_dict))
