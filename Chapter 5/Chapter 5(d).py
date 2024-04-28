a={1,3,4,5,1}
b={2,3,10,12,13}

a.add(4)
a.add(5)
a.add(6)
#a.add([7,8,9]) #---> Can't put a list in a set
a.add((1,7,8,9)) #---> Can put a tupple in a set
#a.add({1:2}) #---> CAn't put a dict in a set
print(a)

print(len(a))

a.remove(5)
print(a)

print(a.pop())
print(a)

print(a.clear()) 