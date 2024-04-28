a=54 #Global Variable
def func():
    global a
    print(a)
    a=8 #Local Variable if global keywoard not used
    print(a)

func()
print(a)