a=12
b=int(input("Enter a num: "))

try:
        print(a/b)
except ZeroDivisionError as e:
    print("infinite")