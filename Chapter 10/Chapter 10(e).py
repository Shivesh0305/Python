class Employee:
    company="Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")
    
    def getDetails(self):
        print(f"The details of the employee are {self.name},{self.salary},{self.subunit}")
    
    def getSalary(self):
        print("Salary is "+ self.salary)

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry=Employee("Harry",100,"Youtube")
harry.getDetails()