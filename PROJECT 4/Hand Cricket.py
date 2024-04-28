import random
a=random.randint(1,6)

print("Get Ready to Play! The rules are simple...\nSame number and you are out!\nScore as many runs as you can, and don't let the computer reach the target!")
toss=input("Heads or tails?\n(Type 1 for Heads and 2 for Tails)")
b=random.randint(1,3)
if b==1:
    if toss=="1":
        print("Heads is the call!...\nAND HEADS IT IS!! You won the toss!")
        choice=input("What would you like to do?Bat first or bowl first?\n(Type 1 to bat and 2 to bowl)")
        if choice=="1":
            print("You decided to bat first! Let's hope for an amazing match!")
            f1=True
        else:
            print("You decided to ball first! Let's hope for an amazing match!")
            f2=True
    else:
        print("Tails is the call!...\nAND IT'S HEADS!! You lose the toss! Computer deciding...")
        compchoice=random.randint(1,3)
        if compchoice==1:
            print("Computer decided to bat first! Let's hope for an amazing match!")
            f="a"
        else:
            print("Computer decided to ball first! Let's hope for an amazing match!")
            f="b"
else:
    if toss=="1":
        print("Heads is the call!...\nAND IT'S TAILS!! You lose the toss! Computer deciding...")
        compchoice=random.randint(1,3)
        if compchoice==1:
            print("Computer decided to bat first! Let's hope for an amazing match!")
            f="c"
        else:
            print("Computer decided to ball first! Let's hope for an amazing match!")
            f="d"
    else:
        print("Tails is the call!...\nAND TAILS IT IS!! You won the toss!")
        choice=input("What would you like to do?Bat first or bowl first?\n(Type 1 to bat and 2 to bowl)")
        if choice=="1":
            print("You decided to bat first! Let's hope for an amazing match!")
            f1=True
        else:
            print("You decided to ball first! Let's hope for an amazing match!")
            f2=True

if f=="a":
    print("LETS BEGIN! YOU HAVE TO BAT!")
    d=None
    a=0
    e=[]
    while a!=d:
        a=random.randint(1,6)
        d=int(input("Your choice: "))
        print("Computer chose: ",a)
        if a!=d and a>1:
            print("You Hit",d,"runs")
        elif a!=d and a==1:
            print("You Hit",d,"run")
        else:
            pass
        e.append(d)
        
        if a==d:
            
            esum1=sum(e[:-1])
            print("And that's a wicket!")
            print("Final Score: ",esum1)
            print("Target: ",int(esum1)+1)
        
    print("Your bowling! Computer will bat!")
    if esum1>=0:
        d=None
        a=0
        e2=[]
        while a!=d:
            a=random.randint(1,6)
            d=int(input("Your choice: "))
            print("Computer chose: ",a)
            if a!=d and d>1:
                print("Computer Hits",a,"runs")
            elif a!=d and d==1:
                print("Computer Hits",a,"run")
            else:
                pass
            e2.append(a)
            esum2=sum(e2)
            if esum2>esum1:
                print("Target Achieved! You Win! Congratulations!")
                break
            elif a==d and esum2<esum1:
                print("And that's a wicket! You got out before reaching the target! You Lose! Better Luck Next Time!")

elif f=="b":
    print("LETS BEGIN! YOU HAVE TO BOWL!")
    d=None
    a=0
    e=[]
    while a!=d:
        a=random.randint(1,6)
        d=int(input("Your choice: "))
        print("Computer chose: ",a)
        if a!=d and a>1:
            print("Computer Hits",a,"runs")
        elif a!=d and a==1:
            print("Computer Hits",a,"run")
        else:
            pass
        e.append(a)
        
        if a==d:
            
            esum1=sum(e[:-1])
            print("And that's a wicket!")
            print("Final Score: ",esum1)
            print("Target: ",int(esum1)+1)
        
    print("Your batting! Computer will bowl!")
    if esum1>=0:
        d=None
        a=0
        e2=[]
        while a!=d:
            a=random.randint(1,6)
            d=int(input("Your choice: "))
            print("Computer chose: ",a)
            if a!=d and d>1:
                print("You Hit",d,"runs")
            elif a!=d and d==1:
                print("You Hit",d,"run")
            else:
                pass
            e2.append(d)
            esum2=sum(e2)
            if esum2>esum1:
                print("Target Achieved! You Win! Congratulations!")
                break
            elif a==d and esum2<esum1:
                print("And that's a wicket! You got out before reaching the target! You Lose! Better Luck Next Time!")

elif f=="c":
    print("LETS BEGIN! COMPUTER HAS TO BAT!")
    d=None
    a=0
    e=[]
    while a!=d:
        a=random.randint(1,6)
        d=int(input("Your choice: "))
        print("Computer chose: ",a)
        if a!=d and a>1:
            print("Computer Hits",a,"runs")
        elif a!=d and a==1:
            print("Computer Hits",a,"run")
        else:
            pass
        e.append(a)
        
        if a==d:
            
            esum1=sum(e[:-1])
            print("And that's a wicket!")
            print("Final Score: ",esum1)
            print("Target: ",int(esum1)+1)
        
    print("Your batting! Computer will bowl!")
    if esum1>=0:
        d=None
        a=0
        e2=[]
        while a!=d:
            a=random.randint(1,6)
            d=int(input("Your choice: "))
            print("Computer chose: ",a)
            if a!=d and d>1:
                print("You Hit",d,"runs")
            elif a!=d and d==1:
                print("You Hit",d,"run")
            else:
                pass
            e2.append(d)
            esum2=sum(e2)
            if esum2>esum1:
                print("Target Achieved! You Win! Congratulations!")
                break
            elif a==d and esum2<esum1:
                print("And that's a wicket! You got out before reaching the target! You Lose! Better Luck Next Time!")

elif f=="d":
    print("LETS BEGIN! YOU HAVE TO BAT!")
    d=None
    a=0
    e=[]
    while a!=d:
        a=random.randint(1,6)
        d=int(input("Your choice: "))
        print("Computer chose: ",a)
        if a!=d and a>1:
            print("You Hit",d,"runs")
        elif a!=d and a==1:
            print("You Hit",d,"run")
        else:
            pass
        e.append(d)
        
        if a==d:
            
            esum1=sum(e[:-1])
            print("And that's a wicket!")
            print("Final Score: ",esum1)
            print("Target: ",int(esum1)+1)
        
    print("Your bowling! Computer will bat!")
    if esum1>=0:
        d=None
        a=0
        e2=[]
        while a!=d:
            a=random.randint(1,6)
            d=int(input("Your choice: "))
            print("Computer chose: ",a)
            if a!=d and d>1:
                print("Computer Hits",a,"runs")
            elif a!=d and d==1:
                print("Computer Hits",a,"run")
            else:
                pass
            e2.append(a)
            esum2=sum(e2)
            if esum2>esum1:
                print("Target Achieved! You Win! Congratulations!")
                break
            elif a==d and esum2<esum1:
                print("And that's a wicket! You got out before reaching the target! You Lose! Better Luck Next Time!")