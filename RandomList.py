import random as r
l=[]
odd=[]
even=[]
x=len(l)
while x<10:
    a=r.randint(1,1000)
    if a not in l:
        l.append(a)
        x+=1
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("complete list is :", l)
print("Even list is: ",even)
print("Odd list is: ",odd)