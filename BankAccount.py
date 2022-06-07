class BankAccount:
    # don't forget to add some default values for these parameters!# your code here! (remember, this is where we specify the attributes for our class)
    def __init__(self, int_rate=0.0, balance=0.0):
        self.int_rate = int_rate
        self.balance = balance
    # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
            self.balance += amount
            return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print(f"Name:{self.name}\nAccount Balance:${self.account_balance}\n")
        return self

    def yield_interest(self):
        # your code herecopy
        # if self.balance > 0:
        self.balance = self.balance * (1 + self.int_rate / 100)
        return self


nora = User('nora', 1000, 1000)
Sara = User('Sara', 1000, 3000)

print('User:Sara')
Sara.make_deposit(400).make_deposit(20).make_deposit(
    10).make_withdrawal(700).yield_interest()
print(Sara.display_user_balance())

print('User:nora')
nora.make_deposit(400).make_deposit(
    20).make_withdrawal(400).make_withdrawal(80).make_withdrawal(200).make_withdrawal(40).yield_interest()
print(lama.display_user_balance())
