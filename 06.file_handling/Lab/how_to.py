#How to find an absolute path :

import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path,'models', 'cars.txt')
file = open(file_path, 'r')
print(file.read())


#How to open , write and close a file with Manager :

import os

file_name = 'text.txt'
absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, file_name)

with open(file_path,'a') as f:
  f.write('blablabla')



#How to open , write and close a file :

import os

file_name = 'text.txt'
absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, file_name)

file = open(file_path, 'a')
file.write('blablabla')
file.close()



#How to delete a file

import os

file_name = 'not_a_file.txt'
root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path,file_name)

if os.path.isfile(file_path):
  os.remove(file_path)
