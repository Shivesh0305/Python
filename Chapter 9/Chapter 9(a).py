f=open("sample.txt","r")  # If mode not defined then read is taken as the default mode
data=f.read() #f.read(5) reads the first 5 characters on the file only
print(data)
f.close()
