from datetime import datetime

class Drinks:
    def __init__(self, name, quantity, price, expiry_date):
        self.name = name
        self.size = quantity
        self.price = price
        self.expiry_date = expiry_date


    def display_info(self):
        return f"Drink: {self.name}, Size: {self.size}, Price: ${self.price:.2f}, Expiry Date: {self.expiry_date}"
    

    def is_expired(self, current_date):
        # Accept strings in 'YYYY-MM-DD' or date objects
        if isinstance(current_date, str):
            current_date = datetime.strptime(current_date, "%Y-%m-%d").date()
        if isinstance(self.expiry_date, str):
            expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        else:
            expiry = self.expiry_date
        return current_date > expiry
    def apply_discount(self, discount_percentage):
        if 0 < discount_percentage < 100:
            discount_amount = (discount_percentage / 100) * self.price
            self.price -= discount_amount
            return f"New price after {discount_percentage}% discount is: ${self.price:.2f}"
        else:
            return "Invalid discount percentage."
# Example usage:
drink = Drinks("Cola", "500ml", 1.50, "2024-12-31")
print(drink.display_info())
print(drink.apply_discount(10))
print("Is the drink expired?", drink.is_expired("2025-01-01"))