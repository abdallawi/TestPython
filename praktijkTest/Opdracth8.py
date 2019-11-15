import ti

class BankAccount:
    balance = 0.0

    def __init__(self, owner):
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


account = BankAccount("Michel")
print(account.owner)
print(account.balance)
account.deposit(235.66)
print(f' Your current balance is : {account.balance}')
account.withdraw(20)
print(f' Your current balance is : {account.balance}')