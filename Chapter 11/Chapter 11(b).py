class Employee():
    company="visa"
    eCode=120

class Freelancer():
    company="Fiverr"
    level=0

    def upgrageLevel(self):
        self.level=self.level + 1

class Programmer(Employee, Freelancer): #---> Name written first is given higher priority
    name="Rohit"

p=Programmer()
p.upgrageLevel()
print(p.level)
print(p.company)