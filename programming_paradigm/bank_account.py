
class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount}"
        else:
           return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            # print("Insufficient funds.")
            return False

    def display_balance(self):
       """Return the current balance as a formatted string."""
       return f"Current Balance: $[{self.__account_balance:.2f}]"
