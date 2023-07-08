import os

while True:
    command, *info = input().split('-')

    if command == 'End':
        break

    if command == 'Create':
        file_name = info[0]

        with open(f'files/{file_name}, "w" '):
            pass

    elif command == 'Add':
        file_name = info[0]
        content = info[1]

        with open(f'files/{file_name}, "a" ') as file:
            file.write(f'{content}\n')

    elif command == 'Replace':
        file_name = info[0]
        old_string = info[1]
        new_string = info[2]

        try:
            with open(f'files/{file_name}, "r+" ') as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek()
                file.write(text)

        except FileNotFoundError:
            print('An error occurred')

    elif command == 'Delete':
        file_name = info[0]

        try:
            os.remove(f'files/{file_name}')

        except FileNotFoundError:
            print('An error occurred')
