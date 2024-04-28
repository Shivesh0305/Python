with open("this.txt") as f:
    a=f.read()

with open("copy.txt",'w') as f:
    f.write(a)