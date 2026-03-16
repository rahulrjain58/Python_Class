print("start")
try:
    a=int(input(("enter a number: ")))
    b=int(input(("enter a number: ")))
    c=a/b
    print("division: ",c)
except ZeroDivisionError as e:
    print(e)
print("End")