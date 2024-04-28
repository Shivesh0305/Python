def square(num):
    return num*num
l=[1,2,3,4]

# Method 1
#l2=[]
#for i in l:
#    l2.append(square(i))
#print(l2)

# Method 2
print(list(map(square,l))) #--->Easier