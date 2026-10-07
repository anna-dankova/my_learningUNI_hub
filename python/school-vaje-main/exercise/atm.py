balance= 1000
while True:
    print("welcome to ATM")
    print("1. check balance")
    print("2. account replenishment")
    print("3. take cash")
    print("4. exit")

    choice=int(input("enter your choice : "))
    if choice==1:
        print(balance)

    elif choice==2:
        print(balance)
        amount=int(input("enter the amount : "))
        balance+=amount
        print(balance)
    elif choice==3:
        print(balance)
        amount=int(input("enter the amount : "))
        balance-=amount
        print(balance)
    elif choise==4:
        break
    else:
        print("invalid choice")
