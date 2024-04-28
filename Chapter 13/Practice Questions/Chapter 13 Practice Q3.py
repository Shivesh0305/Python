l=[]
a=int(input("Enter num "))
for i in range(1,11):
    l.append(str(a*i))

table="\n".join(l)
print(table)