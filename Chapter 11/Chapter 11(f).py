class Employee():
    company="Bharat Gas"
    salary=5000
    salarybonus=1000
    #totalSalary=6000 ---> If any change made to another variable then this will have to be changed too so we don't use this method.

    @property
    def totalSalary(self):
        return self.salary+self.salarybonus
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus=val-self.salary

e=Employee()
print(e.totalSalary)
e.totalSalary=7000
print(e.salary)
print(e.salarybonus)