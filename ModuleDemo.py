import udf

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        a=int(input("Enter your number: "))
        udf.oddeven(a)
    elif choice==2:
        a=int(input("Enter your number: "))
        b=int(input("Enter your number: "))
        udf.maxoftwo(a,b)
    elif choice==3:
        a=int(input("Enter your number: "))
        b=int(input("Enter your number: "))
        c=int(input("Enter your number: "))
        udf.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("Enter your number: "))
        udf.prime(a)
    elif choice==5:
        a=int(input("Enter your number: "))
        udf.fibo(a)
    elif choice==6:
        print("Exiting the system!")
        break
    else:
        print("Invalid Choice, Choose Again!")

    print("*"*40)