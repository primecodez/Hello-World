import random
import string

def password_generator(length=10):
    """Create a function that generates a random password using Python's random library."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":    print(password_generator(8))