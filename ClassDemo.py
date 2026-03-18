# class Student:
#     def getname(self,fname,lname):
#         self.f=fname
#         self.l=lname
#     def putdata(self):
#         print("first name: ",self.f)
#         print("last name: ",self.l)

# s1=Student()
# s1.getname("Rahul","jain")
# s1.putdata()

class Bank:
    def openaccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print(f"Hello {cname} your account no {acno} is opened with {balance} Rs.")
    def deposit(self,amount):
        self.balance=self.balance + amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Inefficient balance")
    def checkbalance(self):
        print(f"Your current balnce is {self.balance} Rs.")

b1=Bank()
b1.openaccount("Rahul Jain",111,5000)

while True:
    print("*"*50)
    print("1. Deposit")
    print("2. withdraw")
    print("3. Checkbalance")
    print("4. Exit")
    choice=int(input("Enter Your choice: "))
    print("*"*50)
    if choice==1:
        amount=int(input("Enter the amount u want to deposit: "))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter the amount u want to withdraw: "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkbalance()
        print("*"*50)
    elif choice==4:
        print("Thank You for choosing our system")
        print("*"*50)
        break
    else:
        print("Invalid choice, Try again")