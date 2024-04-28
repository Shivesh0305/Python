class Employee:
    company="Google"
    salary=100

shivesh=Employee()
harry=Employee()
shivesh.salary="30 Cr" 
harry.salary="30 K"

print(shivesh.company)
print(harry.company)

Employee.company="Youtube"
print(shivesh.company)
print(harry.company)

print(shivesh.salary)
print(harry.salary)