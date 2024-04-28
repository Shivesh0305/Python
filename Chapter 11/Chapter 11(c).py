class Person():
    country="Bharat"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am an employee so I am breathing...")

class programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print("No salary to programmers")

p=Person()
e=Employee()
pr=programmer()

p.takeBreath()
e.takeBreath()
pr.takeBreath()