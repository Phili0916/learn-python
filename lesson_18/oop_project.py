from bank_accounts import *

Phil = BankAccount(1000, "Phil")
Carole = BankAccount(2000, "Carole")

Phil.get_balance()
Carole.get_balance()

Carole.deposit(500)

# Phil.withdraw(100000)
Phil.withdraw(10)

Phil.transfer(50, Carole)

Edward = InterestRewardsAcct(1000, "EdwardAcct")
Edward.get_balance()
Edward.deposit(100)

Martin = SavingsAcct(1000, "MartinAcct")
Martin.get_balance()
Martin.deposit(1000)
Martin.transfer(100, "Carole")