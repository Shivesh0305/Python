file1="this.txt"
file2="copy.txt"

with open(file1) as f:
    a=f.read()    

with open(file2) as f:
    b=f.read()

if a==b:
    print("identical files")
else:
    print("not identical")

