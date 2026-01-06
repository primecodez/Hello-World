import random
import string

def password_generator(length=10):
    """creation a functu=ion that will generate password randomly using random library of python"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

    print(password_generator(8))
    