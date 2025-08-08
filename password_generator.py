import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special = '!@#$&*'

def generate_password(length, use_lower, use_upper, use_digit, use_special):
    """Generate a secure password based on selected character types."""
    pool = ''
    required = []

    if use_lower:
        pool += lower
        required.append(random.choice(lower))
    if use_upper:
        pool += upper
        required.append(random.choice(upper))
    if use_digit:
        pool += digits
        required.append(random.choice(digits))
    if use_special:
        pool += special
        required.append(random.choice(special))

    if not pool:
        raise ValueError("At least one character type must be selected.")

    if length < len(required):
        raise ValueError(f"Password length must be at least {len(required)} characters.")

    remaining = [random.choice(pool) for _ in range(length - len(required))]
    password_list = required + remaining
    random.shuffle(password_list)
    return ''.join(password_list)
