class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__account_holder_name = account_holder_name  # Private attribute
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        return self.__account_balance

# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)

# Test deposit and withdrawal functionality
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # This should print "Insufficient funds or invalid withdrawal amount."

# Display the account balance
print(f"Account Balance for {account._BankAccount__account_holder_name}: ${account.display_balance()}")

