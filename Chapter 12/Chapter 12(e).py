try:
    i=int(input("Enter a num:"))
    c=1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")