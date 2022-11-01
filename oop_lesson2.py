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
        