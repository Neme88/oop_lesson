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