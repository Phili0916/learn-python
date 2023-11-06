class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.acctName = account_name
        print(f"\nAccount {self.acctName} created. \nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount {self.acctName} \nBalance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.get_balance()

    def vialable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry but {self.acctName} only has a balance of {self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        try:
            self.vialable_transaction(amount)
            self.balance = self.balance - amount
            print(f"Withdraw Complete")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")

    def transfer(self, amount, account_name):
        try:
            print('\n**********\n\nBeginning Transfer....💲💵💰')
            self.vialable_transaction(amount)
            self.withdraw(amount)
            self.deposit(amount)
            print("\nTransfer Complete ✅ \n**********")
        except BalanceException as error:
            print(f"\nTransefer interupted ❌ {error}\n************")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete👍")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5
    def withdraw(self, amount):
        try:
            self.vialable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed")
            self.get_balance()
        except BalanceException as error:
            print(f"\nTransefer interupted ❌ {error}\n************")

