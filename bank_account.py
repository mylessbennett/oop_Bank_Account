class BankAccount:
    """ Withdraws, deposits and adds interest to bank account total """

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "---------------\nBalance: {:.2f}\nInterest Rate: {:.1f}%\n---------------".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return

    def gain_interest(self):
        self.balance = self.balance + (self.balance * (self.interest_rate/100))
        return


my_account = BankAccount(100 , 2)

my_account.deposit(100)
print(my_account)

my_account.withdraw(50)
print(my_account)

my_account.gain_interest()
print(my_account)
