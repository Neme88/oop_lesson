#encapsulation
#abstraction
#inheritance
#polymorphosy
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

        