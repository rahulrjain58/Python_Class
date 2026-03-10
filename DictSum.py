import random as r
d={}
OddSum=0
EvenSum=0
for i in range(1,11):
    a=r.randint(1,1000)
    d[i]=a

for a,b in d.items():
    if b%2==0:
        EvenSum+=b
    else:
        OddSum+=b
print("complete list is :", d)
print("Even Sum is: ",EvenSum)
print("Odd Sum is: ",OddSum)