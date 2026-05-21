import re
import math
import string
import os

from config import PATH_TO_BLACKLIST

def password_checker(password: str):
    strength = 0
    reasons = []

    if len(password) < 10:
        reasons.append("- Minimum of 10 characters is required")
    elif len(password) < 13:
        strength += 1
        reasons.append("- Length of 13+ characters is recommended")
    else:
        strength += 2

    digitc = 0

    for char in password:
        if char.isdigit():
            digitc += 1

    if digitc == 0:
        reasons.append("- No digits")
    elif digitc == 1:
        strength += 1
        reasons.append("- Only 1 digit")
    else:
        strength += 2

    lowerc = 0
    upperc = 0

    for char in password:
        if char.isalpha() and char.islower():
            lowerc += 1
        if char.isalpha() and char.isupper():
            upperc += 1

    if lowerc == 0:
        reasons.append("- No lowercase letters")
    elif lowerc == 1:
        strength += 1
        reasons.append("- Only 1 lowercase letter")
    else:
        strength += 2

    if upperc == 0:
        reasons.append("- No uppercase letters")
    elif upperc == 1:
        strength += 1
        reasons.append("- Only 1 uppercase letter")
    else:
        strength += 2

    symbolc = 0

    for char in password:
        if not (char.isalpha() or char.isdigit()):
            symbolc += 1

    if symbolc == 0:
        reasons.append("- No special symbols")
    elif symbolc == 1:
        strength += 1
        reasons.append("- Only 1 speacial symbol")
    else:
        strength += 2

    if bool(re.search(r"(.)\1{2,}", password)):
        strength -= 3
        reasons.append("- Repeated characters")

    if bool(re.search(r"(19|20)\d{2}", password)):
        strength -= 2
        reasons.append("- A year can be related to user")

    if os.path.isfile(PATH_TO_BLACKLIST):
        wordlist = load_wordlist(PATH_TO_BLACKLIST)

        if password.lower() in wordlist:
            strength = 1
            reasons = []
            reasons.append("- Use of highly used common passwords is too dangerous")

    return strength, reasons

def load_wordlist(path: str):
    with open(path, "r", encoding="latin-1") as f:
        return set(line.strip() for line in f)

def entropy_estimate(password: str) -> float:
    pool = 0

    uppers = set(string.ascii_uppercase)
    lowers = set(string.ascii_lowercase)
    digs = set(string.digits)
    symbols = set(string.punctuation)

    if any(c in uppers for c in password):
        pool += 26
    if any(c in lowers for c in password):
        pool += 26
    if any(c in digs for c in password):
        pool += 10
    if any(c in symbols for c in password):
        pool += 32

    if pool == 0:
        pool = len(set(password))
    return float(len(password) * math.log2(pool))
