import random
n = random.randint(0,100)
#print(n)

guess=1
a=None

while a!=n:
    a=int(input("Guess: "))
    if a==n:
        print("You guessed it right!")
        if guess>1:
            print(f"You took {guess} attempts.")
        else:
            print(f"You took {guess} attempt.")
        if guess<=10:
            print("Good job! You are good at guessing!")
        else:
            print("You need to work on your guessing skills. :(")
    else:
        if a<n:
            print("Try again! :(\nHint: It's a greater number.")
        else:
            print("Try again! :(\nHint: It's a smaller number.")
        guess+=1