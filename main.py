def has_digit(password):
    return any(c.isdigit() for c in password)


def has_upper_letters(password):
    return any(c.isupper() for c in password)


def has_lower_letters(password):
    return any(c.islower() for c in password)


def has_symbols(password):
    return any(not c.isdigit() and not c.isalpha() for c in password)


def is_very_long(password):
    return len(password) > 12


password = input("Введите пароль: ")

checks = [
    has_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols,
    is_very_long,
]

score = sum(2 for check in checks if check(password))

print("Рейтинг пароля:", score)