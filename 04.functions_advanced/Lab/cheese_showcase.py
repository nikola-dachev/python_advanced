def sorting_cheeses(**kwargs):
  cheeses_dict = sorted(kwargs.items(),
                         key = lambda kvp:(-len(kvp[1]), kvp[0])
                       )
  result = ''
  for cheese, quantity in cheeses_dict:
    result += cheese + '\n'
    quantity_list =sorted(quantity, reverse = True)
    result += '\n'.join(str(el) for el in quantity_list) + '\n'

  return result

