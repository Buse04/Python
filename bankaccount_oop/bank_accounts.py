class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialmoney:float, name:str):
        self.balance = initialmoney
        self.name = name
        print(f"\nAccount '{self.name}' created. \nBalance = {self.balance:.2f}TL ")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = {self.balance:.2f}TL")
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f"\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has {self.balance:.2f}TL"
            )
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw is finished.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted.\n {error}")
    
    def transfer(self, amount, account):
        try:
            print("\n***************\n\nBeginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer is completed")
        except BalanceException as error:
            print(f"\nTransfer interrupted.\n{error}")

class NewBank(BankAccount):
    pass