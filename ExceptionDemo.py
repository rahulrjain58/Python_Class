print("start")
try:
    a=int(input(("enter a number: ")))
    b=int(input(("enter a number: ")))
    c=a/b
    print("division: ",c)
    l=[1,2,3,4,5,6]
    index=int(input("Enter index number"))
    print(l[index])
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print(e)
except Exception as e:
    print(e)
finally:
    print("finally closed")
print("End")