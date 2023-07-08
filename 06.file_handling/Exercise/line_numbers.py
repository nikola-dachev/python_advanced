import os
from string import punctuation

file_name = 'text.txt'
root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, file_name)

with open(file_path, 'r') as file:
    text = file.readlines()

output_file = open('output.txt', 'w')

for index in range(len(text)):
    letter_counter = 0
    marks_counter = 0

    for symbol in text[index]:
        if symbol.isalpha():
            letter_counter += 1

        elif symbol in punctuation:
            marks_counter += 1

    output_file.write(f'Line {index + 1}: {"".join(text[index][:-1])} {(letter_counter)}{(marks_counter)}')

output_file.close()

