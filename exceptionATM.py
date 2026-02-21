balance=1000
while True:
    print('''===ATM Menu===
    1. Check Balance
    2. Add Money
    3. Withdraw
    4. Exit\n''')
    
    choise=input("choose the operation (1/2/3/4) : ") 
    try:
        if choise=="1":
            print(f"Your balance is : {balance}")
            print("balance fetch successfully\n")

        elif choise=="2":
            add=float(input("enter your deposite ammaunt : "))
            if add <=0:
                raise ValueError("value is  must be greter than zero ")
            balance=add+balance
            print("deposite successfully")
            print(f"your current balance is : {balance} \n")

        elif choise=="3":
            widrawal=float(input("enter your withdraw ammount : "))
            if widrawal <=0:
                raise ValueError("value is  must be greter than zero ")
            if widrawal > balance:
                raise KeyError("insufficient balance")
            balance=balance-widrawal
            print("withdraw successfully")
            print(f"your current balance is : {balance} \n")

        elif choise=="4":
            print("your are Exit successfully\n")
            break
        else:
            print("Invalid choise\n")

    except ValueError as e:
        print("Error :",e)
        
    except KeyError as key:
        print("Error :",key)
     
    