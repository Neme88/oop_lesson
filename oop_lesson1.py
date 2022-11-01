#encapsulation
#abstraction
#inheritance
#polymorphosy
class Bank :
    def __init__(self, bankid, name, location) :
        self.bankid = bankid
        self.name = name
        self.location = location
        self.customers = []
        self.tellers = []
        
    def __str__(self):
        return  f"{self.bankid} {self.name } {self.location}"

x = Bank(45367, "Savvy", "Burgundy")
print(x)
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
            print("your account balance is{i.balance}")
    def deposit_money():
        pass
    def withdraw_money():
        pass
    def open_account():
        pass
    def close_account():
        pass
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
    
class Account :
    def __init__(self, id, customerId) :
        self.id = id
        self.customerId = customerId
        self.balance = 0
class Checking (Account):
    def __init__(self, id, customerId):
        super().__init__(id, customerId)
class Savings (Account):
    def __init__(self, id, customerId):
        super().__init__(id, customerId)       
class Loan :
    def __init__(self, id, type, accountId, customerId,amount) :
        self.id = id
        self.type = type
        self.accountId = accountId
        self.customerId = customerId
        self.amount = amount
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
    
class Account :
    def __init__(self, id, customerId) :
        self.id = id
        self.customerId = customerId
class Checking (Account):
    def __init__(self, id, customerId):
        super().__init__(id, customerId)
class Savings (Account):
    def __init__(self, id, customerId):
        super().__init__(id, customerId)
class Loan :
    def __init__(self, id, type, accountId, customerId) :
        self.id = id
        self.type = type
        self.accountId = accountId
        self.customerId = customerId
        