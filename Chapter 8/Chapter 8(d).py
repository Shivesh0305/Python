#a=4
#b=1
#for i in range(1,a+1):
#    b=b*i
#print(b)

def factorial(num):
    b=1
    for i in range(1,num+1):
        b=b*i
    return(b)

print(factorial(6))

def factorial_recurssive(num):
    if num==1 or num==0:
        return 1
    return num*factorial_recurssive(num-1)

print(factorial_recurssive(6))