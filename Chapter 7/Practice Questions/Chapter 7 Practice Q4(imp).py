a=int(input("Enter a number: "))
prime=True

for i in range(2,a):
    if(a%i==0):
        prime=False
        break
if prime:
    print("Prime number")
else:
    print("Not Prime number")