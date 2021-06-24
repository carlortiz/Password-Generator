# PASSWORD GENERATOR

import random
import string

valid_symbols = ["!", "@", "#", "$", "%",
           "^", "&", "(", ")"]
valid_numbers = ["1", "2", "3", "4", "5",
                 "6", "7", "8", "9"]
new_characters = []

def get_length():
    print("\nEnter the password length")
    length = int(input("Length: "))
    return length

def get_requirement(prompt):
    print("Enter the required amount of", prompt)
    requirement = int(input(prompt.title() + ": "))
    return requirement

def get_characters(requirement, valid_characters):
    for i in range(requirement):
        new_character = random.choice(valid_characters)
        new_characters.append(new_character)

def validate_length(length_requirement):
    if len(new_characters) > length_requirement:
        print("\nError: Required amount of characters "
              "exceeds password length")
        exit()

def fill_out_password(length_requirement):
    while True:
        if len(new_characters) < length_requirement:
            lowercase_letter = random.choice(string.ascii_lowercase)
            new_characters.append(lowercase_letter)
        else:
            break

def main():
    print("You will now enter the requirements for the password.")

    length_requirement = get_length()
    lowercase_requirement = get_requirement("lowercase characters")
    uppercase_requirement = get_requirement("uppercase characters")
    number_requirement = get_requirement("numbers")
    symbol_requirement = get_requirement("symbols")

    get_characters(lowercase_requirement, string.ascii_lowercase)
    get_characters(uppercase_requirement, string.ascii_uppercase)
    get_characters(number_requirement, valid_numbers)
    get_characters(symbol_requirement, valid_symbols)

    validate_length(length_requirement)
    fill_out_password(length_requirement)

    random.shuffle(new_characters)
    password = new_characters[0]

    for char in new_characters:
        if new_characters.index(char) == 0:
            continue
        password = password + char

    print("Your new password is: ", password)

main()
