def  kwargs_length(**kwargs):
  return(len(kwargs))

my_dict = {'one':1, 'two':2}
print(kwargs_length(**my_dict))

