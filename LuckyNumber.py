import random as r

l=[i for i in range(1,100)]
lucky=[]
b=len(lucky)
while b<10:
    a=r.choice(l)
    lucky.append(a)
    l.remove(a)
    b+=1
print(l)
print(lucky)