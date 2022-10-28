#encapsulation
#abstraction
#inheritance
#polymorphosy
class Bank :
    def __init__(self, bankid, name, location) :
        self.bankid = bankid
        self.name = name
        self.location = location
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
    def general_inquiry():
        pass
    def deposit_money():
        pass
    def withdraw_money():
        pass
    def open_account():
        pass
    def close_account():
        pass
    def apply_loan():
        pass
    def request_card():
        pass