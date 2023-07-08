import os

symbols_to_be_replaced = ["-", ",", ".", "!", "?"]

file_name = 'text.txt'
root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path,file_name)

with open(file_path,'r') as file:
  text = file.readlines()

# readlines() gives us a list with the text separated as string for each new line for example:
# i am good
# so good
#['i am good\n', 'so good']

for string in range(0,len(text), 2):
  for symbol in symbols_to_be_replaced:
    text[string] = text[string].replace(symbol, '@')

  print(*text[string].split()[::-1], sep = ' ')
