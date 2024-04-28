with open("Donkey.txt") as f:
    a=f.read()

a=a.replace('Donkey','@#$%@#')

with open("Donkey.txt",'w') as f:
    f.write(a)