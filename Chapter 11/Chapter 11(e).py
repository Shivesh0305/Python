class Employee:
    company="Camel"
    salary=100
    location="Delhi"

    def changeSalary(self,sal):
        self.__class__.salary=sal #---> One method to directly change the class attribute

    @classmethod
    def changeSalary(cls,sal): 
        cls.salary=sal #---> Another method to change the class attribute

e=Employee()
print(e.salary)

e.changeSalary(500)
print(e.salary)
print(Employee.salary)