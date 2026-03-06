import random as r

num=r.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 to 20: "))
    if guess==num:
        print("u guessed the correct number!")
        break
    elif guess>num:
        print("u have guessed the greater number!")
    elif guess < num:
        print("u have guessed the smaller number!")

