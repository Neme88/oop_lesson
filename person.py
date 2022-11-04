class Person :
    def __init__(self, id, name, address, phone_number):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
class Customer (Person):
    def __init__(self, id, name, address, phone_number,account_number):
        super().__init__(id, name, address, phone_number)
        self.account_number =account_number
        self.accounts = []
        self.loans = []
    def general_inquiry(self):
        for i in self.accounts:
            print("your account {i.id}balance is{i.balance}")
    def deposit_money(self, dep_account, amount):
        for account in self.accounts:
            if account.id == dep_account:
                account.balance +=amount
                break  
    def withdraw_money(self, withrd_account, amount):
        checker = 0
        while (checker < len(self.accounts)):
            if accounts[checker].id == withrd_account:
                accounts[checker].balance = account[checker].balance - amount
                break
            checker = checker+1   
    def open_account(self, AccountId):
        self.accounts.append(Account(AccountId, self.id))   
    def close_account(self,accountId):
        for account in self.accounts:
            if account.id == accountId:
                self.accounts.remove(account)
                break
            print("closed account")
            
    def apply_loan(self, amount, type):
        self.loans.append(Loan(0, type, self.accountId, self.id))
    def request_card():
        pass    
class Teller (Person):
    def __init__(self, id, name, address, phone_number):
        super().__init__(id, name, address, phone_number)
    def collectMoney():
        pass
    def openAccount():
        pass
    def closeAccount():
        pass
    def loanRequest():
        pass
    def provideInfo():
        pass
    def issueCard():
        pass
    
