#PAAWORD GENERATOR

import random
import string

letter_list = list(string.ascii_letters)
number_list = list(map(str, range(1, 11)))
symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*']

# User input
length = int(input("Enter the password length you want: "))
character_type = input("Enter character type you want: LETTERS, NUMBERS, SYMBOLS: ").lower()

# Password generation
password = []

if character_type == "letters":
    password.extend(random.sample(letter_list, length))
elif character_type == "numbers":
    password.extend(random.sample(number_list, length))
elif character_type == "symbols":
    password.extend(random.sample(symbol_list, length))
else:
    print("Invalid character type")

random.shuffle(password)

password_str = ''.join(password)

print("Generated Password:", password_str)