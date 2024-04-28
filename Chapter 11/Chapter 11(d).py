class Person():
    country="Bharat"

    def __init__(self):
        print("Initializing Person...")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...")

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so I am breathing...")

class programmer(Employee):
    company="Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...")

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer so I am breathing++...")

#p=Person()
#p.takeBreath()

#e=Employee()
#e.takeBreath()

pr=programmer()
#pr.takeBreath()