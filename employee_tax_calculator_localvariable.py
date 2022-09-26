'''
employee_id=input('enter the id of Employee')
basic_pay=int(input("enter the basic pay of employee"))
def tax_calculation(basicpay):
    tax=0
    if basicpay >25000 and basicpay <= 40000:
        tax= basicpay * (15/100)
    elif basicpay >40000 and basicpay <= 50000:
        tax= basicpay * (18/100)
    elif basicpay >50000:
        tax= basicpay * (20/100)
    return tax 
output=tax_calculation(basic_pay)
print('the calculated tax is',output,'for the employee id=',employee_id)   

'''

from Employee_using_localvariable import Employee
employee_id=input('enter the id of Employee')
basic_pay=int(input("enter the basic pay of employee"))

employee=Employee()
 
tax=employee.calculateTax(basic_pay,employee_id)
print(tax)

annualSalary=employee.getAnnualSalary(basic_pay)
print(annualSalary)


    #print('the calculated tax is',output,'for the employee id=',employee_id)   