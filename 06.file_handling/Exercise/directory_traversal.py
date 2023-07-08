import os


def save_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]

            if extension not in extensions_dict:
                extensions_dict[extension] = []

            extensions_dict[extension].append(file_name)

        if os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = input()
extensions_dict = {}
result = []

save_extensions(directory)

extensions_dict = sorted(extensions_dict.items(), key=lambda x: x[0])

for extensions, files in extensions_dict:
    result.append(f'.{extensions}')

    result.append('\n'.join([f'---{file}' for file in sorted(files)]))

with open('files/report.txt', 'w') as file:
    file.write('\n'.join(result))
