this="   shivesh is good    "
print(this)
print(this.strip())

def strip(str, word):
    newstr=str.replace(word," ")
    return newstr.strip()

print(strip(this, "shivesh"))