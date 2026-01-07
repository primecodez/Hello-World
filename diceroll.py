import random

def roll_dice(sides=6):
    """Simulate rolling a dice with a specified number of sides."""
    dice = random.randint(1, sides)
    return dice
if __name__ == "__main__":
    print(roll_dice(5))