l=[1,2,3,4,5,6,7,8,9,10]
l1=filter(lambda x:x%2==0,l)
print(list(l1))

l2=lambda a,b: str(a)+" is bigger than "+ str(b) if a>b else str(b)+" is bigger than "+str(a)
print(l2(6,5))


l3 = (filter(lambda x: x % (x**3) == 0, l))
print(list(l3))