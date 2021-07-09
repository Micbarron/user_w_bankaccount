from bankaccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    

    def make_deposit(self, amount):
        self.account.balance += amount 
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    

    def display_user_balance(self):
        print(self.account.balance)




Michael = User("Mike Barron", "mike@dojo.com")
Caroline = User("Caroline Barron", "Cbarron47@askjeeves.com")
Sven = User("Sven Johnson", "broOfgus@youtube.com")


# Michael.make_deposit(600).make_deposit(50).make_deposit(350).make_withdrawal(500).display_user_balance()

# Caroline.make_deposit(400).make_deposit(300000000000).make_withdrawal(2).make_withdrawal(40).display_user_balance()

# Sven.make_deposit(1000).make_withdrawal(100).make_withdrawal(60).make_withdrawal(240).display_user_balance()




Michael.make_deposit(1000)
Michael.display_user_balance()
Michael.make_withdrawal(350)
Michael.display_user_balance()


