""" Manages the bank's accounts. """

class Account:
    def __init__(self, name, age, nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

acc_1 = Account("Mahbub", 25, 123456, 1000)
acc_1.deposit(500)
print(acc_1.balance)
acc_1.withdraw(200)
print(acc_1.balance)

