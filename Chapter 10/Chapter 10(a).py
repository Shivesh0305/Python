class RailwayForm:
    formtype="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

shiveshsApplication=RailwayForm()
shiveshsApplication.name="Shivesh"
shiveshsApplication.train="Rajdhani Express"

shiveshsApplication.printData() 