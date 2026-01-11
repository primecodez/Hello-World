""" Creating a program showing balance, deposit, and withdraw functions using OOP concepts """  
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Rs{amount:.2f}. New balance: Rs{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: Rs{amount:.2f}. New balance: Rs{self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return f"Current balance: Rs{self.balance:.2f}"


#Example usage
acc = BankAccount("Rahul", 1000)

acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())
print(acc)
