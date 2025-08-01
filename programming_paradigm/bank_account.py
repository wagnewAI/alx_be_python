# bank_account.py

import os

class BankAccount:
    def __init__(self, balance_file='balance.txt'):
        self.balance_file = balance_file
        self.__account_balance = self.__load_balance()

    def __load_balance(self):
        if os.path.exists(self.balance_file):
            with open(self.balance_file, 'r') as f:
                try:
                    return float(f.read())
                except ValueError:
                    return 0.0
        return 0.0

    def __save_balance(self):
        with open(self.balance_file, 'w') as f:
            f.write(str(self.__account_balance))

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            self.__save_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            self.__save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

