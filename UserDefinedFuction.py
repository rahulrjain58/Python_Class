#Fuction with no argument and no return value
def printLine():
    print("*"*50)
printLine()
print("Welcome to python class")
printLine()
#Fuction with argument and no return value
def add(a,b):
    print(a+b)
printLine()

#Fuction with  argument and  return value
def sub(a,b):
    return a-b
ans=sub(10,4)
print("subtraction is: ",ans)
printLine()

# def test(a=1,b=2,c=3,d=4):
#     print("A: ",a, " B: ",b," C: ",c," D:",d)

# test(b=100,d=200)

def test(a,b,c,*d,**e):
    print("A: ",a, " B: ",b," C: ",c," D:",d, " E: ",e)

test(1,2,3,4,5,6,7,8,9,x=1,y=2,z=3)