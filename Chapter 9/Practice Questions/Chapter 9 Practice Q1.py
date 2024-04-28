with open('poems.txt') as f:
    t=f.read()
if "twinkle" in t:
    print('twinkle is present')
else:
    print('twinkle not present')
