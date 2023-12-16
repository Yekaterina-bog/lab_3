import re

def print_letters(input_string):
    letters = re.findall(r'[a-zA-Z]', input_string)
    for letter in letters:
        print(letter)

input_string = input("Введите строку: ")
print_letters(input_string)