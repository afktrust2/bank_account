class BankAccount:
    bank_name = "Ninja Bank"
    accounts = []
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: {self.balance:.2f}")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insuffient funds. Charging a $5 fee")
        else:
            self.balance -= amount
            print(f"Balance: {self.balance:.2f}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance:.2f}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest 
            print(f"Balance: {self.balance:.2f}")
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()


Mark = BankAccount(0.05, 0)
Kyle = BankAccount(0.01, 0)


print("Mark")
Mark.deposit(1000).deposit(500).withdraw(200).yield_interest().display_account_info()
print("\nKyle")
Kyle.deposit(18170.9).deposit(100).withdraw(1000).withdraw(5000).yield_interest().display_account_info()
print("\n\n")
BankAccount.all_account_info()