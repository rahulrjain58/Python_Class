def oddeven(a):
    if a%2==0:
        print(a, " is Even")
    else:
        print(a, " is Odd")

def maxoftwo(a,b):
    if a>b:
        print(a, " is bigger than ", b)
    else:
        print(b, " is bigger than ", a)

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a, " is bigger than ", b, "& ", c)
        else:
            print(c, " is bigger than ", a, "& ", b)
    elif b>c:
        print(b, " is bigger than ", a, "& ", c)
    else:
        print(c, " is bigger than ", a, "& ", b)

def prime(a):
    if a%2!=0:
        for i in range(3,int(a/2)+1,2):
            if a%i==0:
                print(a, " is not Prime")
                break
        else:
            print(a, " is Prime")
    else:
        print(a, " is not Prime")

def fibo(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()