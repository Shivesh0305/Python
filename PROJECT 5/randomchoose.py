a=[]
b=[]
c=[]
redball=1
import random
r=random.randint(1,4)
if r==1:
    a.append(redball)
elif r==2:
    b.append(redball)
else:
    c.append(redball)
q=input()
if q==1 and len(a)==1:
        print('correct')
elif q==2 and len(b)==1:
        print('correct')
elif q==3 and len(c)==1:
        print('correct')