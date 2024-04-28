class Books:
    Owner="Library"
    contact="7638291083"

    def __init__(self,name,number,location):
        self.name=name
        self.number=number
        self.location=location

    def issue(self):
        import datetime
        d=datetime.datetime.now()
        user=input("Your name: ")
        id=input("Your id: ")
        try:
                print(f"{self.name} is issued to {user}: {id}")
                print(f"Please collect it from {self.location}")
                print(f"Issued on: {d}\nTO BE RETURNED IN NEXT 15 DAYS!")
                print(f"Student library contact number:\n{self.contact}")
        except Exception as e:
                print(f"{self.name} is not available. Please contact the student library.\nContact number: {self.contact}")
        
bookReq=input("Enter the name of the book you wish to issue: ")

Maze_Runner=Books("Maze Runner","AW1234567","Self:1 Row:1")
bookReq.issue()