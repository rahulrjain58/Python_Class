# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\n")


# for i in range(1,5):
#     print(i*"*")

# for i in range(0,5):
#     print(" "*(5-i),end="")
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# for i in range(1,10):
#      print(" "*(9-i),i*" *")

# for i in range(1,10):
#     print()


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("\n")

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("\n")
# L=["A","B","C"]
# for i in range(0,3):
#     for j in range(0,i+1):
#         print(L[i],end="")
#     print("\n")

# for i in range(0,3):
#     for j in range(0,i+1):
#         print(L[j],end="")
#     print("\n")


# for i in range(65,68):
#     for j in range(65,i+1):
#         print(chr(i),end="")
#     print("\n")

# for i in range(65,68):
#     for j in range(65,i+1):
#         print(chr(j),end="")
#     print("\n")


for i in range(2000,3201):
    if i%5==0 and i%7!=0:
        print(i)