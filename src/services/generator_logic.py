import secrets
import string

from services.checker_logic import password_checker

def generate_password(length: int):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    dig = string.digits
    sym = string.punctuation
    all = upper + lower + dig + sym
    new_password = ""

    while True:
        required = [secrets.choice(upper), secrets.choice(upper),
            secrets.choice(lower), secrets.choice(lower),
            secrets.choice(dig), secrets.choice(dig),
            secrets.choice(sym), secrets.choice(sym)
        ]

        remain = []
        for _ in range(length - len(required)):
            remain.append(secrets.choice(all))

        password_list = required + remain
        secrets.SystemRandom().shuffle(password_list)

        new_password = ''.join(password_list)

        strength, _ = password_checker(new_password)
        if strength == 10:
            break
        new_password = ""
    return new_password
