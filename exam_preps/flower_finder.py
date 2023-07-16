from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

my_dict = {"rose": "rose",
           "tulip": "tulip",
           "lotus": "lotus",
           "daffodil": "daffodil"}

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    is_found = False

    for flower in my_dict:
        my_dict[flower] = my_dict[flower].replace(current_vowel, '')
        my_dict[flower] = my_dict[flower].replace(current_consonant, '')

        if not my_dict[flower]:
            print(f"Word found: {flower}")
            is_found = True

        if is_found:
            break

    if is_found:
        break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

