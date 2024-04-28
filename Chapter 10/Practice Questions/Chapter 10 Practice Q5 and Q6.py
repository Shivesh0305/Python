class Trains:

    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def bookTicket(shiv):  #---> Instead of self any other word can also be taken
        print(f"Seats:{shiv.seats}")

    def getStatus(self):
        print(f"Name:{self.name}")

    def fareInfo(self):
        print(f"Fare:{self.fare}")

intercity=Trains("Intercity Express",300,10)

intercity.bookTicket()
intercity.getStatus()
intercity.fareInfo()