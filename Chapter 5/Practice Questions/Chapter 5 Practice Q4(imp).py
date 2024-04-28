s=set()
s.add(20)
s.add(20.0) #---> 20.0 and 20 is same value so only one is printed
s.add("20")
print(s)
print(len(s))