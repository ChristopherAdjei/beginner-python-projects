class BankAccount:
    def __init__(self, customer_name, account_number, balance):
        self.customer_name = customer_name
        self.balance = balance
        self.account_number = account_number

    
    def deposit(self, amount):
        self.balance += self.amount
        return f"Deposit of {amount} is successful | Account has been updated : GHc {self.balance}"


    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Balance is insufficient | Available balance: GHC {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal is successful | Available balance : GHc {self.balance}")


    def get_balance(self):
        return f"Your current balance is: Ghc{self.balance}"


    def customer_details(self):
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Ghc {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, customer_name, account_number, balance, interest_rate):
        super().__init__(customer_name, account_number, balance)
        self.interest_rate = interest_rate

    def interest(self,interest_amt):
        self.interest_amt = self.get_balance() * self.interest_rate / 100
        self.balance += self.interest_amt
        return f"Your interest amount is {interest_amt} | Updated balance is: {self.balance}"

class CurrentAccount(BankAccount):
    def __init__(self, customer_name,account_number, balance, overdraft_limit):
        super().__init__(customer_name, account_number, balance)
        self.overdraft_limit = overdraft_limit


    def check_overdraft(self, amount):
        if (self.balance - amount) >= self.overdraft_limit:
            print(f"Withdrawal denied! Overdraft limit reached.")
        else:
            print("Withdrawal within limit")


class Bank:
    def __init__(self, account_list): 
        self.account_list = account_list    
        

    def add_account(self, account): 
        self.account_list.append(account) 

    def remove_account(self, account_number):
        for account in self.account_list:
            if account.account_number == account_number: 
                self.account_list.remove(account)   
        

    def view_all_accounts(self):
        for account in self.account_list: 
            return f"Account number: {account.account_number}, Balance: {account.balance}, Account name: {account.customer_name}" 
        
ADB = Bank([]) 

account1 = BankAccount("123456", "Akosua", 100) 
account2 = BankAccount("123457", "Ama", 200)
account3 = BankAccount("123458", "Yaa", 600)


ADB.add_account(account1)
ADB.add_account(account2)
ADB.add_account(account3)

print(ADB.view_all_accounts())  

ADB.remove_account("123457")
 
print(ADB.view_all_accounts())