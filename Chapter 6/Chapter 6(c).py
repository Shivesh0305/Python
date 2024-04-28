age=int(input("Enter your age: "))
if(age>34 and age<56):
    print("You can work with us.")
else:
    print("You can't work with us.")

age=int(input("Enter your age: "))
if(age>34 or age<56):
    print("You can work with us.")
else:
    print("You can't work with us.")

age=int(input("Enter your age: "))
if(not age>34):
    print("You can work with us.")
else:
    print("You can't work with us.")