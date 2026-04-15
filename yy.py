class Account:
    def __init__(self, account_number, account_name, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount 
        return f"Deposited {amount}. Your new balance is {self.balance}." 

    def withdrawal(self, amount):
        self.balance -= amount
        return f"Withdrew {amount}. Your new balance is {self.balance}."

    def get_balance(self):
        return f"Your current balance is GH {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_name, account_number, balance, interest_rate): 
        super().__init__(account_name, account_number, balance)
        self.interest_rate = interest_rate
    
    def interest_rate(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount 
        return f"Interest amount {interest_amount}. Your new balance is {self.balance}." 

        

class CurrentAccount(Account):
    def __init__(self, account_name, account_number, balance, overdraft_limit): 
        super().__init__(account_name, account_number, balance)
        self.overdraft_limit = overdraft_limit 

    def check_overdraft(self):
        if self.balance <= 0 and abs(self.balance) > self.overdraft_limit:
            return f"Overdraft limit exceeded." 
        else:
            return f"Overdraft within limit." 


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
            print(f"Name: {account.customer_name}")
            print(f"Account Number: {account.account_number}")
            print(f"Balance: Ghc {account.balance}") 
        
ADB = Bank([]) 

account1 = Account("123456", "Akosua", 100) 
account2 = Account("123457", "Ama", 200)
account3 = Account("123458", "Yaa", 600)


ADB.add_account(account1)
ADB.add_account(account2)
ADB.add_account(account3)

print(ADB.view_all_accounts())  

ADB.remove_account("123457")
 
print(ADB.view_all_accounts())