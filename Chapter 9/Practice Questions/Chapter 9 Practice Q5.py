def censor(word,replace):
    with open("Censor.txt",) as f:
        a=f.read()
    if word in a:
        a=a.replace(word,replace)
        with open("Censor.txt",'w') as f:
            f.write(a)
    else:
        print("Word not in file.")

censor("Donkey","@#$%@$")