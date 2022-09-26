class Employee:
    #def __init__(self,basicpay,id):
        #self.pay=basicpay
        #self.id=id
    def calculateTax(self,basicpay,id):
        tax=0
        if basicpay >25000 and basicpay <= 40000:
            tax= basicpay * (15/100)
        elif basicpay >40000 and basicpay <= 50000:
            tax= basicpay * (18/100)
        elif basicpay >50000:
            tax= basicpay * (20/100)
        return tax
    def getAnnualSalary(self,value):
        return value*12