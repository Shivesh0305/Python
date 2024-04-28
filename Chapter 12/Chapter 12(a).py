while True:
    print("press q to quit")
    a=input("enter a number:")
    if a=="q":
        break
    try:
        a=int(a)
        if a>6:
            print("you entered a number greater than 6")
    except Exception as e:
        print("Your input resulted in an error: ",e)