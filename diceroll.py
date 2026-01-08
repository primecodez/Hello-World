import random



def roll_dice(sides=6):
    """Simulate rolling a dice with a specified number of sides."""
    return random.randint(1, sides)

def dice_game():
    print("Welcome to the Dice Roller game!")

    while True:
        user_choice = input("Roll the dice? (y/n): ").strip().lower()

        if user_choice == 'y':
            print(f"You rolled a {roll_dice()}")
        elif user_choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


dice_game()
