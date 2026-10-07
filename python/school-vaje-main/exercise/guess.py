import random
while True:
    print("welcome to guess the number game")
    print("1. play")
    print("2. exit")
    choice=int(input("enter your choice : "))
    if choice==2:
        break
    print(" number is between 1 and 100")
    number=random.randint(1,100)

    attempts=5

    while attempts>0:
        guess=int(input("enter your guess : "))
        attempts-=1
        if guess<number:
            print("too low")
        elif guess>number:
            print("too high")
        elif guess==number:
            print("congratulations")

        else:
            print("game over")
            break
