
class Transaction:
    def __init__(self, amount, date, customer):
     self.amount =amount
     self.date = date
     self.customer = customer
    
    def printtransction(self):
        print("Amount {0}, Date {1}, Custom {2}".format(self.amount,self.date,self.customer))
    
class CreditTransaction(Transaction):
    def __init__(self,  amount, date, customer, ccn, ccv ):
     self.amount =amount
     self.date = date
     self.customer = customer
     self.ccn = ccn
     self.ccv = ccv
     
    def getCCN(self):
        return self.ccn
    
    def lastfour(self,ccn):
        string = str(ccn) 
        lastfour = string[-4:]
        self.ccn = "XXXXXXXXXXXX" + lastfour
    
    def printcredit(self):
        print("CCN: {0} CCV {1}".format(self.ccn, self.ccv))   
        
class CheckTransaction(Transaction):
    def __init__(self,  amount, date, customer, checknumber, routing ):
     self.amount =amount
     self.date = date
     self.customer = customer
     self.routing = routing
     self.checknumber = checknumber
     
    def printcheck(self):
        print("Check Number: {0} Routing Number {1}".format(self.checknumber, self.routing))
        

def main():
    transactions = Transaction(22.23, "2/2/2020", "Awesome Cutomer")
    transactions.printtransction()
    
    credit = CreditTransaction(8892.92, "2/1/2020", "Awesome Cutomer", 1234567823232345, 321)
    credit.lastfour(credit.getCCN())
    credit.printcredit()
    credit.printtransction()
    
    check = CheckTransaction(444.44, "1/11/2020", "Bob", 4212, 810022301)
    check.printcheck()
    check.printtransction()

main()