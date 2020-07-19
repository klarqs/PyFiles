class Account(object):
    def __init__(self, account_number, account_name, account_type):
        self.account_balance = 0
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount

    def check_balance(self):
        return self.account_balance

    def __str__(self):
        description = "Account Info\n=========\n"
        description += "Name: {}\n"
        description += "Type: {}\n"
        description += "Number: {}\n"
        description += "Balance: {}\n"

        return description.format(
            self.account_name,
            self.account_type,
            self.account_number,
            self.account_balance
        )


iClass = Account(123456789, "iClass", "Savings")
print(iClass)

print("\nChecking balance")
print(iClass.check_balance())

print("\nDeposit 100")
print(iClass.deposit(100))

print("\nChecking balance")
print(iClass.check_balance())

print("\nWithdraw 10")
print(iClass.withdraw(10))

print("\nChecking balance")
print(iClass.check_balance())

print(iClass)
