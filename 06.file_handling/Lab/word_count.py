import os
import re
from collections import defaultdict


def read_content(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print('File is not found')


words_file_name = 'words.txt'
words_root_path = os.path.dirname(os.path.abspath(__file__))
words_file_path = os.path.join(words_root_path, words_file_name)

text_file_name = 'text.txt'
text_root_path = os.path.dirname(os.path.abspath(__file__))
text_file_path = os.path.join(text_root_path, text_file_name)

words = read_content(words_file_path).lower().split()

text_content = read_content(text_file_path).lower()
text_content = re.sub(r'[^\w+\s]', '', text_content)
text_lines_content = text_content.split('\n')

words_count_dict = defaultdict(lambda: 0)
for word in words:
    for line in text_lines_content:
        if word in line:
            words_count_dict[word] += 1

for key, value in sorted(words_count_dict.items(), key=lambda kvp: -kvp[1]):
    print(f'{key} - {value}')
