from employee import Employee

class Company:
    def __init__(self):
        self.employess=[]

    def add_employee(self,new_emmployess):
        self.employess.append(new_emmployess)
    def print_employee(self):
        print("current Employees:")
        for i in self.employess:

            print("Employee first name:",i.fname,"Employee last name", i.lname, "Salary",i.salary)
    def pay_employee(self):
        print('paying Employee:')
        for i in self.employess:
            print("paycheck for ", i.fname, i.lname)
            print(f"Amount:${i.calculate_paycheck():,.2f}")
def main():
    my_company = Company()
    employee1= Employee("Srinibash", 'sahu',50000)
    my_company.add_employee(employee1)
    employee2= Employee("Srinibash_1", 'sahu',60000)
    my_company.add_employee(employee2)
    employee3= Employee("Srinibash_2", 'sahu',60000)
    my_company.add_employee(employee3)
    employee4= Employee("Srinibash_3", 'sahu',60000)
    my_company.add_employee(employee4)
    # print(my_company.employess)
    my_company.print_employee()
    my_company.pay_employee()
    
main()