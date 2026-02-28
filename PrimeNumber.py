# n=int(input("Enter a Number: "))
# Flag=True
# for i in range(2,n):
#     if n%i==0:
#         Flag=False

# if Flag:
#     print("Number is Prime Number")
# else:
#     print("Number is Not a Prime Number")


n=int(input("Enter a Number: "))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n," is not a prime number")
            break
    else:
        print(n," is a prime number")
else:
    print(n," is not a prime number")

