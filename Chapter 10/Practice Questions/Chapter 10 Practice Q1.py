class Programmers:
    company="Microsoft"
    salary=100
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The info of the programmers are {self.name},{self.product}")

harry=Programmers("Harry","Office")
Amit=Programmers("Amit","Office")

harry.getInfo()