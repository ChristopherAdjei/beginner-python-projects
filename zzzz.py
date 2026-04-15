class BankAccount:
    def __init__(self, customer_name, account_number, balance = 0):
        self.customer_name = customer_name
        self.balance = balance
        self.account_number = account_number

    
    def deposit(self, amount):
            self.balance += amount
            print(f"GhC{amount} has been deposited into your account")


    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Balance is insufficient")
        else:
            self.balance -= amount
            print(f"GhC{amount} has been withdrawn from your account")


    def get_balance(self):
        print(f"Your current balance is: Ghc{self.balance}")


    def customer_details(self):
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Ghc{self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, customer_name, account_number, balance, interest_rate):
        super().__init__(customer_name, account_number, balance)
        self.interest_rate = interest_rate

class Bank:
    def __init__(self):
        self.account_list = []

    def add_account(self, account):
        (self.customer_name, self.account_number, self.balance) = account
        self.account_list.append(account)

    def remove_account(self, account_number):
        for account in self.account_list:
            (self.customer_name, self.account_number, self.balance) = account
            if self.account_number == account_number:
                self.account_list.remove(account)

    def view_all_account(self):
        for account in self.account_list:
            (self.customer_name, self.account_number, self.balance) = account 
            print(f"Name: {self.customer_name}")
            print(f"Account Number: {self.account_number}")
            print(f"Balance: Ghc {self.balance}")

