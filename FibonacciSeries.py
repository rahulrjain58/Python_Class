# n=int(input("Enter a Number: "))
# F_Num=0
# S_Num=1
# print(F_Num)
# print(S_Num)
# while n>2:
#     L_Num=F_Num+S_Num
#     F_Num=S_Num
#     S_Num=L_Num
#     n-=1
#     print(L_Num)


n=int(input("Enter a Number: "))
a,b=0,1
print(a,end=" ")
while b<n:
    print(a,end=" ")
    a,b=b,a+b
