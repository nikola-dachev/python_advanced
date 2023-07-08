import os

file_name = 'my_first_file.txt'
absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, file_name)

with open(file_path,'a') as f:
  f.write('I just created my first file!')
