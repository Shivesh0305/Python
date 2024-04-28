a=[3,4,5,6,7,8,9,10,11,12]

#b=[]
#for i in a:
#    if i%2==0:
#        b.append(i)

#print(b)
#---> To save this effort we use the following:-

b=[i for i in a if i%2==0]
print(b)