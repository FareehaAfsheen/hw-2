class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show(self):
        print("Name:", self.name)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited amount:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawn Amount:", amount)

    def get_balance(self):
        return self.__balance


def find_account(accounts, name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None

accounts = []

while True:
    print('\n --Bank Management System--')
    print("1. Add Account")
    print("2. Show All Accounts")
    print("3. Check Balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer Money")
    print("7. Delete Account")
    print("8. Exit")