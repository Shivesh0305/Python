list1=[3,53,2,False,6.2,"Harry"]

#index=0
#for items in list1:
#    print(items, index)
#    index+=1
#---> To save all this effort we use enumerate function

for index,item in enumerate(list1):
    print(index,item)