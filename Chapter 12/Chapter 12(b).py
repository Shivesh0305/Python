try:
    a=int(input("Enter a number "))
    c=1/a
    print(c)
except ValueError as e:
    print("Exception1 occured")
    print(e)

except ZeroDivisionError as e:
    print("Exception2 occured")
    print(e)