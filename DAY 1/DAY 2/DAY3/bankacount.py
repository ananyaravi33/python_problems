class BankAccount:

    def __init__(self, name, accn, balance):
        self.name = name
        self.accn = accn
        self.__balance = balance   # private variable

    # Getter
    def getBalance(self):
        return self.__balance

    # Setter
    def setBalance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

    # Deposit using setter logic
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Withdraw using getter logic
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


# Creating object
acc1 = BankAccount("Bavi", 123, 1000)

# Using getter
print("Initial Balance:", acc1.getBalance())

# Using setter
acc1.setBalance(2000)
print("Updated Balance:", acc1.getBalance())

# Using deposit & withdraw
acc1.deposit(500)
acc1.withdraw(700)

print("Final Balance:", acc1.getBalance())
