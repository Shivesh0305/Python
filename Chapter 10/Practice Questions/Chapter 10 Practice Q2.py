class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(self.num*self.num)

    def cube(self):
        print(self.num*self.num*self.num)

    def root(self):
        print(self.num**1/2)

a=Calculator(4)

a.square()
a.cube()
a.root()