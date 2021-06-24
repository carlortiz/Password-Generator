# PASSWORD VALIDATOR

valid_symbols = ["!", "@", "#", "$", "%",
                 "^", "&", "(", ")"]
requirements = []

LENGTH_LIMIT = 12
LOWER_CASE_LIMIT = 5
UPPER_CASE_LIMIT = 1
NUMBER_LIMIT = 2
SYMBOL_LIMIT = 1

MODERATE_PASSWORD = 3
FAIRLY_STRONG_PASSWORD = 4
VERY_STRONG_PASSWORD = 5


def get_password():
    print("Enter a password to be checked for strength")
    password = input("Password: ")
    return password


def check_if_symbol(char):
    for symbol in valid_symbols:
        if char == symbol:
            return True
    return False


def validate_limit(count, limit):
    if count >= limit:
        requirements.append(True)
    requirements.append(False)


def get_password_strength(requirements_met):
    if requirements_met == VERY_STRONG_PASSWORD:
        return "VERY STRONG"
    elif requirements_met == FAIRLY_STRONG_PASSWORD:
        return "FAIRLY STRONG"
    elif requirements_met == MODERATE_PASSWORD:
        return "MODERATE"
    return "WEAK"


def main():
    password = get_password()

    password_length = len(password)
    lower_cases = 0
    upper_cases = 0
    numbers = 0
    symbols = 0

    for char in password:
        if char.islower():
            lower_cases += 1
        elif char.isupper():
            upper_cases += 1
        elif char.isnumeric():
            numbers += 1
        elif check_if_symbol(char):
            symbols += 1

    validate_limit(password_length, LENGTH_LIMIT)
    validate_limit(lower_cases, LOWER_CASE_LIMIT)
    validate_limit(upper_cases, UPPER_CASE_LIMIT)
    validate_limit(numbers, NUMBER_LIMIT)
    validate_limit(symbols, SYMBOL_LIMIT)

    requirements_met = 0
    for requirement in requirements:
        if requirement:
            requirements_met += 1

    password_strength = get_password_strength(requirements_met)
    print("Your password is", password_strength)

main()
