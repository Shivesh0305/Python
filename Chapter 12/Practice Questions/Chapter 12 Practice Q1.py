try:
    with open("1.txt") as f:
        f.read()
    with open("2.txt") as f:
        f.read()
    with open("3.txt") as f:
        f.read()
except Exception as e:
    print(e)