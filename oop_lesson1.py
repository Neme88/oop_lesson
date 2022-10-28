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