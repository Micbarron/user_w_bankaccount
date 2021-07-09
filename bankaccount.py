
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("Innsuficient Funds")
            return self        
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"{self} Balance :{self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += self.balance  * self.int_rate
            return self

            

# account123 = BankAccount(.02, 0)
# account456 = BankAccount(.02, 0)

# account123.deposit(100).deposit(300).deposit(400).withdrawal(650).display_account_info()
# account123.yeild_interest()
# account123.display_account_info()

# account456.deposit(5000)
# account456.deposit(450)
# account456.withdrawal(5)
# account456.withdrawal(57)
# account456.withdrawal(154)
# account456.withdrawal(1234)
# account456.display_account_info()
# account456.yeild_interest()
# account456.display_account_info()


