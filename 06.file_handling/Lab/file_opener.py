import os

abs_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(abs_path, 'text.txt')

if os.path.isfile(file_path):
    print('File found')

else:
    print('File not found')
