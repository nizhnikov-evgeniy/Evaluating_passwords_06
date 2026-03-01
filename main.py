MIN_LENGTH = 12
SCORE_PER_CHECK = 2


def is_very_long(password):
    return len(password) >= MIN_LENGTH


def has_digit(password):
    return any(c.isdigit() for c in password)


def has_upper_letters(password):
    return any(c.isupper() for c in password)


def has_lower_letters(password):
    return any(c.islower() for c in password)


def has_symbols(password):
    return any(not c.isdigit() and not c.isalpha() for c in password)


def get_password_score(password):
    score = 0

    checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    for check in checks:
        if check(password):
            score += SCORE_PER_CHECK

    return score


def main():
    password = input("Введите пароль: ")
    score = get_password_score(password)
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
