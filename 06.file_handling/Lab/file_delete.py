import os

file_name = 'my_first_file.txt'
root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path,file_name)

if os.path.isfile(file_path):
  os.remove(file_path)
else:
  print('File already deleted!')
