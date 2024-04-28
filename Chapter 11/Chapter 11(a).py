class Employee():
    company="Google"

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language="Python"
    company="Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e=Employee()
p=Programmer()

e.showDetails()
p.showDetails()