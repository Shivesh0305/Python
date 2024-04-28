def summition(n):
    if n<0:
        return 0
    return n+summition(n-1)

print(summition(6))