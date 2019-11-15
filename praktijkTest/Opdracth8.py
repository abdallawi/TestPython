class BankAccount:
    balance = 0.0

# Constructor raise an exception if the name of the owner is not a string of min 3 characters
    def __init__(self, owner):
        if not isinstance(owner, str) or len(owner) < 3:
            raise ValueError('The owner name must be a string of min 3 letters')
        else:
            self.owner = owner.title()

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Function that withdraws the requested amount and returns the new balance
# Raise an exception if the asked amount is bigger than the balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f'The amount demanded must be inferior than your balance :  {self.balance}')
        else:
            self.balance -= amount
        return self.balance


try:
    account = BankAccount("sue")
except ValueError as ve:
    print(ve)

print(f'The owner of this account is : {account.owner}')
account.deposit(235.66)

print(f'Your current balance of {account.owner} is : {account.balance}')
try:
    account.withdraw(256)
except ValueError as ve:
    print(ve)
print(f'Your current balance of {account.owner} is :{account.balance}')