import string
import random


def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Основной набор символов
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Генерация пароля
    password = "".join(random.choice(characters) for _ in range(length))
    return password
