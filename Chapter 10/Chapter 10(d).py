class Employee:
    company="Google"
    def getSalary(self):
        print("Salary is "+ self.salary)

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry=Employee()
#harrygetSalary()=Employee.getSalary(harry)
harry.greet() #Employee.greet() ---> without 'self'
