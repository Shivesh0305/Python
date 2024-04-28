def greatest_num(n1,n2,n3):
    if n1>n2:
        f1=n1
    else:
        f1=n2
        if f1>n3:
            f2=f1
        else:
            f2=n3
        return f2
    
print(greatest_num(1,5,2))
