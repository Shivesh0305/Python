a={"snake","water","gun"}

f1=input("Enter Your Move: ") # PLAYER 1
f2=a.pop() # PLAYER 2

print("You Chose "+f1)
print("Computer Chose "+f2)

if f1=="snake" and f2=="gun":
    print("Gun defeats Snake. Computer wins.")
elif f1=="snake" and f2=="water":
    print("Snake defeats Water. You win.")
elif f1=="gun" and f2=="water":
    print("Water defeats Gun. Computer wins.")
elif f1=="gun" and f2=="snake":
    print("Gun defeats Snake. You win.")
elif f1=="water" and f2=="snake":
    print("Snake defeats Water. Computer wins.")
elif f1=="water" and f2=="gun":
    print("Water defeats Gun. You win.")
else:
    print("Draw")