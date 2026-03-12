import random as r

data = open("data.txt","w")
for i in range(10):
    data.write(str(r.randint(1,100))+",")
data.close()
data=open("data.txt","r")
Even=open("even.txt","w")
Odd=open("odd.txt","w")
Prime=open("prime.txt","w")
l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        Even.write(i+",")
        if int(i)==2:
            Prime.write(i+",")
    else:
        Odd.write(i+",")
        for x in range(3,int(int(i)/2)+1,2):
            if int(i)%x == 0:
                break
        else:
            if i=="1":
                break
            else:
                Prime.write(i+",")
    
data.close()
Even.close()
Odd.close()
Prime.close()

data=open("data.txt","r")
Even=open("even.txt","r")
Odd=open("odd.txt","r")
Prime=open("prime.txt","r")

print("Data Files Content is: ", data.read())
print("Even Files Content is: ", Even.read())
print("Odd Files Content is: ", Odd.read())
print("Prime Files Content is: ", Prime.read())


data.close()
Even.close()
Odd.close()
Prime.close()