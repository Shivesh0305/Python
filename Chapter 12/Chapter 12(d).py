try:
    i=int(input("Enter a num:"))
    c=1/i
except Exception as e:
    print(e)
else:
    print("We were successful")